import yfinance as yf

'''
Positions are stored as 
Ticker, [Buy Price, Amount], Buy Time
'''

class StockTracker():

	def __init__(self):
		self.positionLogReader = csv.reader(open('positions.csv', 'w'))

		indexDict = {}
		for i in range(len(positionLogReader)):
			indexDict[positionLogReader[i][0]] = i # indexDict[ticker] = listPosition
		self.tickerIndex = indexDict

	def getPrice(self):
		info = yf.Ticker("MSFT").info
		ask = float(info['ask']) # Lowest a seller will accept
		bid = float(info['bid']) # Highest a seller will accept
		return(round((ask+bid)/2, 2))

	def updatePosition(self, ticker):
		for row in self.positionLogReader:


	def buyStock(self):
		pass

if __name__ == '__main__':
	st = StockTracker()
	print(st.getPrice())