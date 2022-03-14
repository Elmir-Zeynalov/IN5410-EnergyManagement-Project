class Appliance:
    def __init__(self, name, daily_usage, min_consumption, max_hourly_consumption, type):
        self.name = name
        self.daily_usage = daily_usage
        self.min_consumption = min_consumption
        self.max_hourly_consumption = max_hourly_consumption
        self.type = type

    def print_appliance(self):
        return self.name, self.min_consumption, self.max_hourly_consumption, self.type
