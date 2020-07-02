import csv

from Scrapers import finvizScraper as finviz
from determineSentiment import determineSentiment

logFilePath = finviz.scrapePage('FIZZ')

with open(logFilePath) as logFile:
	reader = csv.reader(logFile)

	rowNo = 0
	for row in reader:
		if rowNo == 0: # The first row is a header with row values
			pass
		rowNo+=1
	
		date = row[0]
		time = row[1]
		headline = row[2]

		sentiment = determineSentiment(headline)
		if sentiment > 0:
			buyStock
		elif sentiment < 0:
			sellstock