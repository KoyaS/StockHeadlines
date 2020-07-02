from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import sys
import os

'''
Scrapes webpage for headlines of a given stock ticker. 
When using, DO NOT call this script rapidly out of respect for the site owners.

run using command:
	`python3 finvisScraper.py ticker`
	`python finvisScraper.py ticker`

Writes results out to a csv in relative directory /FinVis/${ticker}/${currentTime}.csv
where:
	ticker 			= 	stock ticker
	current time 	= 	time program is run

'''

def scrapePage(ticker):
	current_time = datetime.now().strftime("%H-%M-%S") # Current time will be name of log file
	pathTo = 'FinVis/'+ticker # Folder log file is stored in
	fileName = current_time+'.csv' # Log file name
	fullPath = pathTo +'/'+ fileName

	if not os.path.exists('pathTo'):
		try:
			os.makedirs(pathTo)
		except FileExistsError:
			pass

	csv_out = open(fullPath, 'w')
	csv_writer = csv.writer(csv_out)
	csv_writer.writerow(['date', 'time', 'headline'])

	# html_out = open('html_out.html', 'w') # For debugging
	# html_in = open('html_out.html', 'r') # For debugging
	# response = html_in # For debugging

	# Get webpage raw html and convert to string
	print('Requesting page for ticker: ' + ticker)
	req = Request(url='https://finviz.com/quote.ashx?t='+ticker, headers={'user-agent': 'app/0.0.1'})
	response = urlopen(req)  
	html = BeautifulSoup(response, 'lxml') # Html string

	# print('writing out html...') # For debugging
	# html_out.write(str(html)) # For debugging

	# BS instance 
	soup = BeautifulSoup(str(html), 'lxml')
	tables = soup.find_all('table')

	# tables[32] is the element which holds a list of the other html elements that
	# contain times and headlines, extract and write out here
	dateHolder = ''
	for tableRow in tables[32].find_all('tr'):

		time = tableRow.find_all('td')[0].text
		if len(time.split(' ')) > 1:
			dateHolder = time.split(' ')[0]
			time = time.split(' ')[1]

		headline = tableRow.find_all('td')[1].find('a').text

		csv_writer.writerow([dateHolder, time, headline])

	return(fullPath)

if __name__ == '__main__':
	TICKER = str(sys.argv[1]) # Get stock ticker from command line argument
	scrapePage(TICKER)


