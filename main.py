import logging
import sys

from oanda.oanda import Order
from oanda.oanda import APIClient

import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    api_client = APIClient(access_token=settings.access_token, account_id=settings.account_id)
    # from functools import partial
    #
    # def trade(ticker):
    #     print(ticker.mid_price)
    #     print(ticker.ask)
    #     print(ticker.bid)
    #
    # callback = partial(trade)
    # ticker = api_client.get_realtime_ticker(callback)

    order = Order(
        product_code=settings.product_code,
        side='SELL',
        units=10
    )

    api_client.send_order(order)