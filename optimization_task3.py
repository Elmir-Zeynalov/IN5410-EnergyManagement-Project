import random
from re import I, X

import numpy as np

from Appliance import Appliance
from Appliance_Type import appliance_type
from scipy.optimize import linprog
from Household import Household
from PriceGenerators import RTP_Price


NUMBER_OF_HOUSES = 30
HOURS_IN_DAY = 24
EV_MAX_HOURLY = 3


def get_houses_with_ev(num_houses):
    houses_with_EVs = []
    for _ in range(num_houses):
        houses_with_EVs.append(random.randint(0, 1))
    return houses_with_EVs


def main():
    houses_with_EVs = get_houses_with_ev(NUMBER_OF_HOUSES)
    number_of_appliances = sum(houses_with_EVs)

    left_eq = []
    households = []
    for i in range(NUMBER_OF_HOUSES):
        house = Household("House " + str(i))
        households.append(house)
        if (houses_with_EVs[i] == 0):
            left_eq.append([0] * HOURS_IN_DAY * NUMBER_OF_HOUSES)
            continue

        ev = Appliance("EV", 9.9, 0, EV_MAX_HOURLY, appliance_type.shiftable)
        house.add_appliance(ev)
        left_eq.append(ev.set_operation_time(
            20, 8, HOURS_IN_DAY, NUMBER_OF_HOUSES))

    # Sets daily usage of household to daily usage of it's appliances
    rhs_eq = []
    for house in households:
        appliances = house.get_appliances()
        if len(appliances) == 0:
            rhs_eq.append(0)
        else:
            rhs_eq.append(appliances[0].daily_usage)

    ineq_matrix = np.identity(HOURS_IN_DAY * NUMBER_OF_HOUSES)

    rhs_ineq = [EV_MAX_HOURLY] * HOURS_IN_DAY * NUMBER_OF_HOUSES

    rtp = RTP_Price(HOURS_IN_DAY, NUMBER_OF_HOUSES)
    objective = rtp.get_rtp_prices()

    opt = linprog(c=objective, A_ub=ineq_matrix,
                  b_ub=rhs_ineq, A_eq=left_eq, b_eq=rhs_eq, method="revised simplex")

    print('Optimized consumption for the EV each hour House # 1:', np.round(opt.x[:25], 2),
          '\nOptimized consumption for the EV each hour House # 2', np.round(
              opt.x[25:49], 2),
          '\nOptimized consumption for the EV each hour House # 3', np.round(
              opt.x[48:72], 2),
          '\nTotal Optamized cost for the nebougherhood in NOK', np.round(opt.fun, 2))


if __name__ == '__main__':
    main()
