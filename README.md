# woofipro-python
Python SDK (sync and async) for Woofipro cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/woofipro)
- You can check Woofipro's docs here: [Docs](https://www.google.com/search?q=google+woofipro+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/woofipro-python
- Pypi package: https://pypi.org/project/woofipro-api


## Installation

```
pip install woofipro-api
```

## Usage

### Sync

```Python
from woofipro import WoofiproSync

def main():
    instance = WoofiproSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from woofipro import WoofiproAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = WoofiproAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from woofipro import WoofiproWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = WoofiproWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_balance(self, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposits_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_interval(self, symbol: str, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe: str = '1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position(self, symbol: Str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_status(self, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fees(self, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids: List[str], symbol: Str = None, params={})`
- `describe(self)`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `get_asset_history_rows(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `get_withdraw_nonce(self, params={})`
- `hash_message(self, message)`
- `nonce(self)`
- `set_leverage(self, leverage: int, symbol: Str = None, params={})`
- `set_sandbox_mode(self, enable: bool)`
- `withdraw(self, code: str, amount: float, address: str, tag: Str = None, params={})`

### REST Raw

- `v1_public_get_public_volume_stats(request)`
- `v1_public_get_public_broker_name(request)`
- `v1_public_get_public_chain_info_broker_id(request)`
- `v1_public_get_public_system_info(request)`
- `v1_public_get_public_vault_balance(request)`
- `v1_public_get_public_insurancefund(request)`
- `v1_public_get_public_chain_info(request)`
- `v1_public_get_faucet_usdc(request)`
- `v1_public_get_public_account(request)`
- `v1_public_get_get_account(request)`
- `v1_public_get_registration_nonce(request)`
- `v1_public_get_get_orderly_key(request)`
- `v1_public_get_public_liquidation(request)`
- `v1_public_get_public_liquidated_positions(request)`
- `v1_public_get_public_config(request)`
- `v1_public_get_public_campaign_ranking(request)`
- `v1_public_get_public_campaign_stats(request)`
- `v1_public_get_public_campaign_user(request)`
- `v1_public_get_public_campaign_stats_details(request)`
- `v1_public_get_public_campaigns(request)`
- `v1_public_get_public_points_leaderboard(request)`
- `v1_public_get_client_points(request)`
- `v1_public_get_public_points_epoch(request)`
- `v1_public_get_public_points_epoch_dates(request)`
- `v1_public_get_public_referral_check_ref_code(request)`
- `v1_public_get_public_referral_verify_ref_code(request)`
- `v1_public_get_referral_admin_info(request)`
- `v1_public_get_referral_info(request)`
- `v1_public_get_referral_referee_info(request)`
- `v1_public_get_referral_referee_rebate_summary(request)`
- `v1_public_get_referral_referee_history(request)`
- `v1_public_get_referral_referral_history(request)`
- `v1_public_get_referral_rebate_summary(request)`
- `v1_public_get_client_distribution_history(request)`
- `v1_public_get_tv_config(request)`
- `v1_public_get_tv_history(request)`
- `v1_public_get_tv_symbol_info(request)`
- `v1_public_get_public_funding_rate_history(request)`
- `v1_public_get_public_funding_rate_symbol(request)`
- `v1_public_get_public_funding_rates(request)`
- `v1_public_get_public_info(request)`
- `v1_public_get_public_info_symbol(request)`
- `v1_public_get_public_market_trades(request)`
- `v1_public_get_public_token(request)`
- `v1_public_get_public_futures(request)`
- `v1_public_get_public_futures_symbol(request)`
- `v1_public_post_register_account(request)`
- `v1_private_get_client_key_info(request)`
- `v1_private_get_client_orderly_key_ip_restriction(request)`
- `v1_private_get_order_oid(request)`
- `v1_private_get_client_order_client_order_id(request)`
- `v1_private_get_algo_order_oid(request)`
- `v1_private_get_algo_client_order_client_order_id(request)`
- `v1_private_get_orders(request)`
- `v1_private_get_algo_orders(request)`
- `v1_private_get_trade_tid(request)`
- `v1_private_get_trades(request)`
- `v1_private_get_order_oid_trades(request)`
- `v1_private_get_client_liquidator_liquidations(request)`
- `v1_private_get_liquidations(request)`
- `v1_private_get_asset_history(request)`
- `v1_private_get_client_holding(request)`
- `v1_private_get_withdraw_nonce(request)`
- `v1_private_get_settle_nonce(request)`
- `v1_private_get_pnl_settlement_history(request)`
- `v1_private_get_volume_user_daily(request)`
- `v1_private_get_volume_user_stats(request)`
- `v1_private_get_client_statistics(request)`
- `v1_private_get_client_info(request)`
- `v1_private_get_client_statistics_daily(request)`
- `v1_private_get_positions(request)`
- `v1_private_get_position_symbol(request)`
- `v1_private_get_funding_fee_history(request)`
- `v1_private_get_notification_inbox_notifications(request)`
- `v1_private_get_notification_inbox_unread(request)`
- `v1_private_get_volume_broker_daily(request)`
- `v1_private_get_broker_fee_rate_default(request)`
- `v1_private_get_broker_user_info(request)`
- `v1_private_get_orderbook_symbol(request)`
- `v1_private_get_kline(request)`
- `v1_private_post_orderly_key(request)`
- `v1_private_post_client_set_orderly_key_ip_restriction(request)`
- `v1_private_post_client_reset_orderly_key_ip_restriction(request)`
- `v1_private_post_order(request)`
- `v1_private_post_batch_order(request)`
- `v1_private_post_algo_order(request)`
- `v1_private_post_liquidation(request)`
- `v1_private_post_claim_insurance_fund(request)`
- `v1_private_post_withdraw_request(request)`
- `v1_private_post_settle_pnl(request)`
- `v1_private_post_notification_inbox_mark_read(request)`
- `v1_private_post_notification_inbox_mark_read_all(request)`
- `v1_private_post_client_leverage(request)`
- `v1_private_post_client_maintenance_config(request)`
- `v1_private_post_delegate_signer(request)`
- `v1_private_post_delegate_orderly_key(request)`
- `v1_private_post_delegate_settle_pnl(request)`
- `v1_private_post_delegate_withdraw_request(request)`
- `v1_private_post_broker_fee_rate_set(request)`
- `v1_private_post_broker_fee_rate_set_default(request)`
- `v1_private_post_broker_fee_rate_default(request)`
- `v1_private_post_referral_create(request)`
- `v1_private_post_referral_update(request)`
- `v1_private_post_referral_bind(request)`
- `v1_private_post_referral_edit_split(request)`
- `v1_private_put_order(request)`
- `v1_private_put_algo_order(request)`
- `v1_private_delete_order(request)`
- `v1_private_delete_algo_order(request)`
- `v1_private_delete_client_order(request)`
- `v1_private_delete_algo_client_order(request)`
- `v1_private_delete_algo_orders(request)`
- `v1_private_delete_orders(request)`
- `v1_private_delete_batch_order(request)`
- `v1_private_delete_client_batch_order(request)`

### WS Unified

- `describe(self)`
- `watch_public(self, messageHash, message)`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe: str = '1m', since: Int = None, limit: Int = None, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `authenticate(self, params={})`
- `watch_private(self, messageHash, message, params={})`
- `watch_private_multiple(self, messageHashes, message, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `set_positions_cache(self, client: Client, type, symbols: Strings = None)`
- `load_positions_snapshot(self, client, messageHash)`
- `watch_balance(self, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.