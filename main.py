from stock_prices import StockPrices
from news import News
from message_client import MessageClient

# STEP 1: Use https://www.alphavantage.co
stock_prices = StockPrices()
stock_prices.get_price_difference()
difference = round(stock_prices.difference, 2)
diff_percentage = round(stock_prices.diff_percentage, 2)

if diff_percentage >= 0.05:
    #get News
    news = News()
    news.get_headlines()
    news.clean_text()
    formatted_articles = news.headlines

    message = ""
    # price increased
    if stock_prices.difference < 0:
        message = f"{stock_prices.stock_name}: 🔺{diff_percentage}%\n"
    else:
        message = f"{stock_prices.stock_name}: 🔻{diff_percentage}%\n"

    message_client = MessageClient()
    for article in formatted_articles:
        message_client.send_alert(message + article)
        break
