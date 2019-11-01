# class will be passed the array of data
# will call analyse method to calculate best profit, buy time and sell time
class StockAnalyser:
    def __init__(self, stockMarket):
        self.buyTime = stockMarket[0]
        self.sellTime = stockMarket[1]
        self.bestProfit = stockMarket[1]-stockMarket[0]
        self.stockMarket = stockMarket

    def Analyse(self):

        bestLowIdx = 0

        for idx, stock in enumerate(self.stockMarket[1:]):  # start at second element
          if stock < stockMarket[bestLowIdx]:
              #print(idx)
              bestLowIdx = idx+1 # need + 1 and starting at [1:]
          if (stock - stockMarket[bestLowIdx]) > self.bestProfit:
              self.sellTime = idx+1 # need + 1 and starting at [1:]
              self.buyTime = bestLowIdx   
              self.bestProfit = stock - stockMarket[bestLowIdx]

    def GetBuyTime(self):
        return self.buyTime
    
    def GetSellTime(self):
        return self.sellTime

    def GetBestProfit(self):
        return self.bestProfit

    def GetStockMarket(self):
        return self.stockMarket

# data array of stocks
stockMarket = (2,2,5,9,5,6,8,8,1)

stockBroker = StockAnalyser(stockMarket)
stockBroker.Analyse()

print("Broker has been looking at data provided: ")
print(stockBroker.GetStockMarket())
profitText = "Broker says the biggest profit you could have made was {}" 
print(profitText.format(stockBroker.GetBestProfit()))
buySellTimeText = "For this you would have had to buy at [{}] and sell at [{}]"
print(buySellTimeText.format(stockBroker.GetBuyTime(), stockBroker.GetSellTime()))






''' this method only stores the values and not the indexes of the share prices
    def Analyse(self):
        bestLow = stockMarket[0]

        for stock in self.stockMarket[1:]:  # start at second element
          if stock < bestLow:
              bestLow = stock
          if (stock - bestLow) > self.bestProfit:
              self.sellTime = stock
              self.buyTime = bestLow   
              self.bestProfit = self.sellTime - self.buyTime
        #endmethod '''   