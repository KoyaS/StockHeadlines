#Test

from bs4 import BeautifulSoup
import requests as rq
import csv
import sys

i = int(sys.argv[1])

csv_out = open('seekingalpha_scrape.csv', 'w')
csv_writer = csv.writer(csv_out)
csv_writer.writerow(['pageNum', 'ticker', 'headline', 'time'])

html_out = open('html_out.html', 'w')

print('Requesting page ' + str(i) + '...')

source = rq.get('https://seekingalpha.com/market-news/all?page=' + str(i))
print('writing out...')
html_out.write(str(source.content))
soup = BeautifulSoup(source.content, 'lxml')
list = soup.find('ul', class_='mc-list')

for tickerRow in list.find_all('li', class_='mc'):

	foundTicker = False

	# Get tickers ~160
	divWrapper = tickerRow.find('div', 'media-left')
	if divWrapper != None:
		tickerLink = divWrapper.find('a')
		if tickerLink != None:
			foundTicker = True
			tickerString = tickerLink.text
			# print(tickerLink.text)

	if foundTicker:

		divWrapper = tickerRow.find('div', 'media-body')

		# Get headline
		titleWrapper = divWrapper.find('div', class_='title')
		titleString = titleWrapper.find('a').text
		# print(titleString)

		timeWrapper = divWrapper.find('div', class_='mc-share-info')
		timeString = timeWrapper.find('span', 'item-date').text
		# print(timeString)

		csv_writer.writerow([i, tickerString, titleString, timeString])



'''
If divWrapper != None, but tickerLink == None,
the row is a news article not about a specific stock
'''

# for listElement in soup.find_all('li', class_='mc'):
# 	a = listElement.find('div', 'media-left')
# 	# b = listElement.find('div', 'media-body')


# 	print("a: ", a)
# 	print(a.find_all('a'))
# 	# print("body: ", b)