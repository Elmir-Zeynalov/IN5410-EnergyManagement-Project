from Household import Household
from Appliance import Appliance
from Appliance_Type import appliance_type
from scipy.optimize import linprog
from PriceGenerators import ToU_Price
import numpy as np

HOURS_IN_DAY = 24


def main():
    house_1 = Household("House 1")

    # This household has only 3 appliances (Washing Machine, EV, Dishwasher)
    washing_machine = Appliance("Washing Machine", 1.94,
                                0, 1.5, appliance_type.shiftable)
    ev = Appliance("EV", 9.9, 0, 3.0, appliance_type.shiftable)
    dishwasher = Appliance("Dishwasher", 1.44, 0, 1.2,
                           appliance_type.shiftable)

    house_1.add_appliance(washing_machine)
    house_1.add_appliance(ev)
    house_1.add_appliance(dishwasher)

    house_1.print_household()
    house_1.print_appliances()

    rhs_eq = [i.daily_usage for i in house_1.get_appliances()]

    # Setting up LHS for optimization problem (equality)
    ws_schedule = washing_machine.set_operation_time(
        7, 23, HOURS_IN_DAY, len(house_1.appliances))
    ev_schedule = ev.set_operation_time(
        0, 7, HOURS_IN_DAY, len(house_1.appliances))
    dw_schedule = dishwasher.set_operation_time(
        12, 18, HOURS_IN_DAY, len(house_1.appliances))

    left_eq = []
    left_eq.append(ws_schedule)
    left_eq.append(ev_schedule)
    left_eq.append(dw_schedule)

    """
    print("Left eq:")
    for i in range(len(left_eq)):
        print("A:",i, ":", *left_eq[i])
    """

    ineq_matrix = np.identity(HOURS_IN_DAY * len(house_1.get_appliances()))

    """
    print("\nLeft ineq")
    for i in range(len(ineq_matrix)):
        print(i,":",*ineq_matrix[i])
    """

    rhs_ineq = []
    for value in house_1.get_appliances():
        rhs_ineq += [value.max_hourly_consumption] * HOURS_IN_DAY

    ToU = ToU_Price()
    objective = ToU.get_ToU_prices(HOURS_IN_DAY) * len(house_1.appliances)

    opt = linprog(c=objective, A_ub=ineq_matrix,
                  b_ub=rhs_ineq, A_eq=left_eq, b_eq=rhs_eq, method="revised simplex")

    x = opt.x
    print(x)

    schedules = [x[i:(i+24)] for i in range(0, len(x), 24)]
    for appliance in house_1.get_appliances():
        print(appliance.name, schedules[appliance.index])

    print('Total optimized cost for the household in NOK',
          np.round(opt.fun, 2))


if __name__ == '__main__':
    main()
