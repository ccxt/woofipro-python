import os
import sys
import asyncio

# if CCXT is included locally
# sys.path.append(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) + '/')

from woofipro import WoofiproAsync

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = WoofiproAsync({})
    await instance.load_markets()
    symbol = "BTC/USDC"

    # fetch ticker
    ticker = await instance.fetch_ticker(symbol)
    print(ticker)

    # create order
    order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 123456.789)
    print(order)

    # close after you finish
    await instance.close()

asyncio.run(main())

