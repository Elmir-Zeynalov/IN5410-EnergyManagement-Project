class Appliance:
    index_counter = 0

    def __init__(self, name, daily_usage, min_consumption, max_hourly_consumption, type):
        self.name = name
        self.daily_usage = daily_usage
        self.min_consumption = min_consumption
        self.max_hourly_consumption = max_hourly_consumption
        self.type = type
        self.index = Appliance.index_counter
        Appliance.index_counter += 1

    def _add_padding(self, pading_left, appliance_usage, hours):
        if pading_left == True:
            padded_result = [0] * hours + appliance_usage
        else:
            padded_result = appliance_usage + [0] * hours
        return padded_result

    def set_operation_time(self, start, end, hours_in_day, appliance_count) -> list[int]:
        daily_usage = [0] * hours_in_day
        for i in range(len(daily_usage)):
            if (i >= start or i < end):
                daily_usage[i] = 1

        for _ in range(self.index):
            daily_usage = self._add_padding(True, daily_usage, hours_in_day)

        for _ in range(appliance_count - 1 - self.index):
            daily_usage = self._add_padding(False, daily_usage, hours_in_day)

        return daily_usage

    def print_appliance(self):
        return self.name, self.min_consumption, self.max_hourly_consumption, self.type, self.index
