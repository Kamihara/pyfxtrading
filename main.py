import logging
import sys

from oanda.oanda import APIClient

import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    api_client = APIClient(
        access_token=settings.access_token, account_id=settings.account_id
    )
    ticker = api_client.get_ticker(product_code=settings.product_code)
    print(ticker.product_code)
    print(ticker.timestamp)
    print(ticker.bid)
    print(ticker.ask)
    print(ticker.volume)
