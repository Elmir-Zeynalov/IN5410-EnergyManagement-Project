from Household import Household
from Appliance import Appliance
from Appliance_Type import appliance_type

def init_non_shiftable_appliances(household):
    lighting = Appliance("Lighting", 2.0, 1.0, 0.5, appliance_type.non_shiftable)
    heating = Appliance("Heating", 9.6, 6.4, 2.2, appliance_type.non_shiftable)
    refrigerator_freezer = Appliance("Refrigerator", 3.96, 1.32, 1.0, appliance_type.non_shiftable)
    electric_stove = Appliance("Electric stove", 3.9, 0, 2, appliance_type.non_shiftable)
    tv = Appliance("TV", 0.3, 0, 0.05, appliance_type.non_shiftable)
    computer = Appliance("Computer", 0.6, 0, 0.2, appliance_type.non_shiftable)

    household.add_appliance(lighting)
    household.add_appliance(heating)
    household.add_appliance(refrigerator_freezer)
    household.add_appliance(electric_stove)
    household.add_appliance(tv)
    household.add_appliance(computer)

def init_shiftable_appliances(household):
    dishwasher = Appliance("Dishwasher", 1.44, 0, 1.2,appliance_type.shiftable)
    washing_machine = Appliance("Washing Machine", 1.94, 0, 1.5, appliance_type.shiftable)
    dryer = Appliance("Dryer", 2.50, 0, 1.2, appliance_type.shiftable)
    ev = Appliance("EV", 9.9, 0, 3.0, appliance_type.shiftable)

    household.add_appliance(dishwasher)
    household.add_appliance(washing_machine)
    household.add_appliance(dryer)
    household.add_appliance(ev)

#Hair dryer, Coffee Machine, Ceiling Fan
def init_random_appliances_case_1(household):
    hair_dryer = Appliance("Hair dryer", 0.893, 0, 0.975, appliance_type.shiftable)
    coffee_machine = Appliance("Coffee machine", 0.6, 0, 0.12, appliance_type.shiftable)
    ceilling_fan = Appliance("Ceiling fan", 0.43, 0, 0.14, appliance_type.shiftable)
    #microwave = Appliance("Microwave", 0.6, 0, 1.2, appliance_type.shiftable)
    #cell_charger = Appliance("Cell charger", 0.006, 0, 0.005, appliance_type.shiftable)

    household.add_appliance(hair_dryer)
    household.add_appliance(coffee_machine)
    household.add_appliance(ceilling_fan)

#Coffee Machine, Microwave, Cell charger.
def init_random_appliances_case_2(household):
    coffee_machine = Appliance("Coffee machine", 0.6, 0, 0.12, appliance_type.shiftable)
    microwave = Appliance("Microwave", 0.6, 0, 1.2, appliance_type.shiftable)
    cell_charger = Appliance("Cell charger", 0.006, 0, 0.005, appliance_type.shiftable)

    household.add_appliance(coffee_machine)
    household.add_appliance(microwave)
    household.add_appliance(cell_charger)
