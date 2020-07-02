from textblob import TextBlob
import sys

def determineSentiment(sentence):
	blob = TextBlob(sentence)
	return(blob.sentiment.polarity)

if __name__ == '__main__':
	print(determineSentiment(str(sys.argv[1])))
