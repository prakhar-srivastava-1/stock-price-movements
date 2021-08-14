import requests
from secrets import NEWSAPI_API_KEY, NEWSAPI_ENDPOINT


class News:
    def __init__(self):
        self.headlines = list()

    def get_headlines(self):
        parameters = {
            "q": "tesla",
            "apiKey": NEWSAPI_API_KEY,
        }
        response = requests.get(NEWSAPI_ENDPOINT, params=parameters)
        response.raise_for_status()

        self.headlines = response.json()["articles"][:3]

    def clean_text(self):
        text_headlines = [f"Headline: {headline['title']}.\n" \
                          f"Brief: {headline['description']}"
                          for headline in self.headlines]
        self.headlines = text_headlines
