import sys
import woofipro.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from woofipro.ccxt import woofipro as WoofiproSync
from woofipro.ccxt.async_support.woofipro import woofipro as WoofiproAsync
from woofipro.ccxt.pro.woofipro import woofipro as WoofiproWs
