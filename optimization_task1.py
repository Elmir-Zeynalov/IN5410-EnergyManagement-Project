from Household import Household
from Appliance import Appliance
from Appliance_Type import appliance_type
from scipy.optimize import linprog
import numpy as np

house_1 = Household("House 1")

# This household has only 3 appliances (Washing Machine, EV, Dishwasher)
washing_machine = Appliance("Washing Machine", 1.94,
                            0, 1.5, appliance_type.shiftable)
ev = Appliance("EV", 9.9, 0, 3.0, appliance_type.shiftable)
dishwasher = Appliance("Dishwasher", 1.44, 0, 1.2, appliance_type.shiftable)

house_1.add_appliance(washing_machine)
house_1.add_appliance(ev)
house_1.add_appliance(dishwasher)

house_1.print_household()
house_1.print_appliances()
print()

rhs_eq = [1.94, 9.9, 1.44]
schedule = []
h = 23
appliance_count = 3


def price_ToU(hour):
    return 1 if 17 <= hour <= 20 else 0.5


def set_operation_time(appliance, start, end):
    daily_usage = [0] * h
    daily_usage[start:end] = [1] * (end - start)

    for i in range(appliance):
        daily_usage = add_padding(True, daily_usage)

    for i in range(appliance_count - 1 - appliance):
        daily_usage = add_padding(False, daily_usage)

    return daily_usage


def add_padding(pading_left, appliance_usage):
    if pading_left == True:
        padded_result = [0] * h + appliance_usage
    else:
        padded_result = appliance_usage + [0] * h
    return padded_result


def max_power_per_hour(hours, count_appliance):
    """
    Adding vectors for hourly max energy use for the appliances.
    """
    left_inequalities = []
    for i in range(count_appliance):
        for j in range(hours):
            lst = [0] * (count_appliance * h)
            lst[j + hours * i] = 1
            left_inequalities.append(lst)
    return left_inequalities


# Setting up LHS for optimization problem
ws_usage = set_operation_time(0, 7, 23)
ev_usage = set_operation_time(1, 0, 7)
dw_usage = set_operation_time(2, 12, 18)

left_eq = []
left_eq.append(ws_usage)
left_eq.append(ev_usage)
left_eq.append(dw_usage)

"""
print("Left eq:")
for i in range(len(left_eq)):
    print("A:",i, ":", *left_eq[i])
"""

ineq_matrix = max_power_per_hour(h, appliance_count)

"""
print("\nLeft ineq")
for i in range(len(ineq_matrix)):
    print(i,":",*ineq_matrix[i])
"""

rhs_ineq = []
rhs_ineq_values = [1.5, 3.0, 1.8]
for value in rhs_ineq_values:
    rhs_ineq += [value] * h

objective = [price_ToU(i) for i in range(h)] * appliance_count

opt = linprog(c=objective, A_ub=ineq_matrix,
              b_ub=rhs_ineq, A_eq=left_eq, b_eq=rhs_eq, method="revised simplex")

x = opt.x

xx_xx = [x[i:(i+24)] for i in range(0, len(x), 24)]

print(x)
