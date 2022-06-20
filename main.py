# 1. A trade executor... This code is like an API, you can talk to it and ask it to buy or sell some stocks or crypto for you. Its hooked up to exchanges, has API keys, and knows how much stocks/crypto you have. 
# 2. A trade bot... This code like "makes decisions" in real time. Its deciding every second or every minute if it should buy or sell or do nothing. If it decides to buy and sell, it'll send a message to the trade executor to do something.
# 3. A backtesting code. This code will accept various trade bots, and allow you to do parameterized back tests with different variables and let you compare and analyze the results to determine how good your strategy is..

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(GOOG, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
print(stats)
bt.plot()