import backtrader
import datetime
from strategies import TestStrategy

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(1000000)

# data = backtrader.feeds.YahooFinanceCSVData(
#     dataname='data/oracle.csv',
#     # Do not pass values before this date
#     fromdate=datetime.datetime(2000, 1, 1),
#     # Do not pass values after this date
#     todate=datetime.datetime(2000, 12, 31),
#     reverse=False)

data = backtrader.feeds.GenericCSVData(
    dataname='data/ohlc/AAPL.txt',
    fromdate=datetime.datetime(2017, 3, 1),
    todate=datetime.datetime(2021, 2, 18),

    nullvalue=0.0,

    dtformat=('%Y-%m-%d'),

    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    openinterest=6,

)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()