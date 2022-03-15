class Household:
    appliances = []

    def __init__(self, name):
        self.name = name

    """
    Adds an appliance to the households list of appliances
    """

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    """
    Funciton to print the households name
    """

    def print_household(self):
        print("Household name is:", self.name)

    """
    Function to print all the appliances that belong to a household
    """

    def print_appliances(self):
        for count, appliance in enumerate(self.appliances):
            print(str(count) + " : " + str(appliance.print_appliance()))
        print()

    def get_appliances(self):
        return self.appliances
