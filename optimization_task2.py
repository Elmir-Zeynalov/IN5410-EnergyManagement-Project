from Household import Household
from Appliance import Appliance
from Appliance_Type import appliance_type
from RTPPriceGenerator import RTP_Price
from optimization_task2_init import *

HOURS_IN_DAY = 24



house_case_1 = Household("House - Case 1")
init_non_shiftable_appliances(house_case_1)
init_shiftable_appliances(house_case_1)
init_random_appliances_case_1(house_case_1)

house_case_1.print_household()
house_case_1.print_appliances()

print("Checking random price generator:")
rtp = RTP_Price()
print(rtp.get_rtp_prices(), '\n')

#Case 1
"""
- Hair dryer usable hour 45 mins, 9am –9.45am.
- Coffee machine usable hour, 20 min, 6am- 6.20am.
- Coffee machine use 2: 10 min, 17.00-17.10
- Fan usable hour 22.00 to 9.00
"""
appliances = house_case_1.get_appliances()

#non-shiftable
lighting_schedule = appliances[0].set_operation_time(
    10, 20, HOURS_IN_DAY, len(house_case_1.appliances))
heating_schedule = appliances[1].set_operation_time(
    0, 24, HOURS_IN_DAY, len(house_case_1.appliances))
refrigerator_freezer_schedule = appliances[2].set_operation_time(
    0, 24, HOURS_IN_DAY, len(house_case_1.appliances))
electric_stove_schedule = appliances[3].set_operation_time(
    18, 19, HOURS_IN_DAY, len(house_case_1.appliances))
tv_schedule = appliances[4].set_operation_time(
    17, 22, HOURS_IN_DAY, len(house_case_1.appliances))
computer_schedule = appliances[5].set_operation_time(
    21, 23, HOURS_IN_DAY, len(house_case_1.appliances))

#shiftable
dishwasher_schedule = appliances[6].set_operation_time(
    21, 24, HOURS_IN_DAY, len(house_case_1.appliances))
washing_machine_schedule = appliances[7].set_operation_time(
    17, 24, HOURS_IN_DAY, len(house_case_1.appliances))
dryer_schedule = appliances[8].set_operation_time(
    0, 6, HOURS_IN_DAY, len(house_case_1.appliances))
ev_schedule = appliances[9].set_operation_time(
    0, 7, HOURS_IN_DAY, len(house_case_1.appliances))

#random appliances
"""
#issue with using floats
hair_dryer_schedule = appliances[10].set_operation_time(
    9, 9.75, HOURS_IN_DAY, len(house_case_1.appliances))
coffee_machine_schedule = appliances[11].set_operation_time(
    6, 6.34, HOURS_IN_DAY, len(house_case_1.appliances))
coffee_machine_schedule = appliances[11].set_operation_time(
    17, 17.17, HOURS_IN_DAY, len(house_case_1.appliances))
"""
hair_dryer_schedule = appliances[10].set_operation_time(
    9, 10, HOURS_IN_DAY, len(house_case_1.appliances))
coffee_machine_schedule = appliances[11].set_operation_time(
    6, 7, HOURS_IN_DAY, len(house_case_1.appliances))
coffee_machine_schedule = appliances[11].set_operation_time(
    17, 18, HOURS_IN_DAY, len(house_case_1.appliances))
fan_schedule = appliances[12].set_operation_time(
    0, 9, HOURS_IN_DAY, len(house_case_1.appliances))
fan_schedule = appliances[12].set_operation_time(
    22, 24, HOURS_IN_DAY, len(house_case_1.appliances))


left_eq = []
left_eq.append(lighting_schedule)
left_eq.append(heating_schedule)
left_eq.append(refrigerator_freezer_schedule)
left_eq.append(electric_stove_schedule)
left_eq.append(tv_schedule)
left_eq.append(computer_schedule)

left_eq.append(dishwasher_schedule)
left_eq.append(washing_machine_schedule)
left_eq.append(dryer_schedule)
left_eq.append(ev_schedule)

left_eq.append(hair_dryer_schedule)
left_eq.append(coffee_machine_schedule)
left_eq.append(coffee_machine_schedule)
left_eq.append(fan_schedule)
left_eq.append(fan_schedule)


print(lighting_schedule)

#Case 2
"""
- Coffee machine use 30 mins, 17.00-17.30
- Microwave use 1: 15 mins, 11-11.15
- Microwave use 2: 5 mins, 17.40-17.05
- Microwave use 3: 10 mins, 18.00-18.10
- Cell charger: 120 mins, 3.00 -5.00 am
"""
