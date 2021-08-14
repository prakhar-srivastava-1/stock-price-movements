from secrets import ALPHAVANTAGE_ENDPOINT, ALPHAVANTAGE_API_KEY
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


class StockPrices:

    def __init__(self):
        self.stock_data = self.get_json_data()
        self.difference = 0.00
        self.diff_percentage = 0.00
        self.stock_name = STOCK

    @staticmethod
    def get_json_data():
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK,
            "apikey": ALPHAVANTAGE_API_KEY
        }
        response = requests.get(ALPHAVANTAGE_ENDPOINT, params=parameters)
        response.raise_for_status()
        return response.json()["Time Series (Daily)"]

    def get_price_difference(self):

        today = dt.datetime.now().date()
        time_delta = dt.timedelta(days=1)
        yesterday = today - time_delta
        day_before = yesterday - time_delta

        data_yesterday = self.stock_data[str(yesterday)]
        data_day_before = self.stock_data[str(day_before)]

        self.difference = float(data_day_before["4. close"]) - float(data_yesterday["4. close"])
        self.diff_percentage = abs(self.difference/float(data_day_before["4. close"])) * 100
