import random


class RTP_Price:
    rtp_prices = []

    def __init__(self, hours_in_day=24, number_of_houses=1):
        RTP_Price.rtp_prices = self._generate_rtp_prices(
            hours_in_day, number_of_houses)

    """
    Random price curve generator.
    * Peak hours:
        - 17:00 to 20:00
        - 07:00 to 08:00
    """

    def _generate_rtp_prices(self, hours_in_day, number_of_houses):
        generated_prices = []
        for j in range(hours_in_day):
            if j >= 17 and j <= 20:
                price = random.uniform(115, 150)
            elif j >= 7 and j <= 8:
                price = random.uniform(120, 160)
            else:
                price = random.uniform(105, 120)
            generated_prices.append(price)
        return generated_prices * number_of_houses

    def get_rtp_prices(self):
        return self.rtp_prices


class ToU_Price:
    def get_ToU_prices(self, hours_in_day):
        prices = []
        for i in range(hours_in_day):
            prices.append(1 if 17 <= i <= 20 else 0.5)

        return prices
