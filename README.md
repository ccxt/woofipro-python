# woofipro-python
Python SDK (sync and async) for Woofipro with Rest and WS capabilities.

You can check Woofipro's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/woofipro)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install woofipro-api
```

## Usage

### Async

```Python
from woofipro_api import WoofiproAsync

async def main():
    instance = WoofiproAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from woofipro_api import WoofiproSync

def main():
    instance = WoofiproSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from woofipro_api import WoofiproWs

async def main():
    instance = WoofiproWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

