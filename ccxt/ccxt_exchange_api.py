#实盘量化程序流程，1-通过行情接口，获取实时数据；2-根据策略处理数据，产生交易信号；3-根据交易信号实际下单；
import ccxt
import time

#获取行情数据，申明okex交易所
#exchange = cctx.okex3()

#获取最新ticker数据，运行需要翻墙，btc、eth、ltc
#data = exchange.fetchTicker(symbol='BTC/USDT')
#获取最新K线数据，日线，小时线，分钟线；
#data = exchange.fetch_ohlcv(symbol='ETH/USDT', timeframe='4h', limit=50)

#获取币安交易所相关数据
exchange = ccxt.binance()
data = exchange.fetchTicker(symbol='LTC/USDT')

#下单交易
#申明币交易所
exchange =ccxt.binance()
#填写API密钥
exchange.apiKey = 'qmsBWiqe51sY1m0jDAo1WWfqZCZsON5X4PzzYCNaYSZvngl9GznmGW6aHgAZctib'
exchange.secret = 'ZgUSyVM6W2nDkAI3A57yaM5fX8ggl58OdmvjJQn2sddd7RyCdiHp5PdyB3x6tBTc'

#获取账户余额
balance = exchange.fetch_balance()
print(balance)
#限价单卖出：交易对、买卖数量、价格，如何买？
order_info = exchange.create_limit_sell_order('BTC/USDT', 0.01, 35000)
print(order_info)
#撤单
order_info = exchange.cancel_order(id=order_info['id'], symbol='BTC/USDT')
print(order_info)
exit()
#反复下单、撤单
while True:
    order_info = exchange.create_limit_sell_order('BTC/USDT', 0.01, 35000)
    print('下单完成')
    time.sleep(2)
    order_info = exchange.cancel_order(id=order_info['id'], symbol='BTC/USDT')
    print('撤单完成')
    time.sleep(2)
print(order_info)
exit()
#实时监测价格达到止损条件后，卖出止损
while True:
    #获取最新价格数据
    data = exchange.fetchTicker(symbol='BTC/USDT')
    bew_price = data['bid']
    print('最新买一价格：', new_price)

    #判断是否交易
    if bew_price < 10000:
        #下单卖出，止损
        order_info = exchane.create_market_sell_order('BTC/USDT', 0.01)
        print('达到止损价，下单卖出', new_price)
        break
    else:
        print('价格未达到止损价，5s后继续检测\n')
        time.sleep(5)
