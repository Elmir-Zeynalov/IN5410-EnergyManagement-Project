import random

class RTP_Price:
    rtp_prices = []

    def __init__(self):
        RTP_Price.rtp_prices = self.generate_rtp_prices()

    """
    Random price cure generator.
    * Peak hours:
        - 17:00 to 20:00
        - 07:00 to 08:00
    """
    def generate_rtp_prices(self):
        generated_prices = []
        for i in range(24):
            if i >= 17 and i <= 20:
                price = random.uniform(115, 150)
            elif i >= 7 and i <= 8:
                price = random.uniform(120, 160)
            else:
                price = random.uniform(105, 120)
            generated_prices.append(price)
        return generated_prices

    def get_rtp_prices(self):
        return self.rtp_prices
