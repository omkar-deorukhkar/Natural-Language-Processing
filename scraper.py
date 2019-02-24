import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from sys import argv

class Analysis:
	def __init__(self,term):
		self.term1 = term + ' ' + 'moneycontrol' 
		self.term2 = term + ' ' + 'nse'
		self.term3 = 'india economy'
		self.subjectivity = 0
		self.sentiment = 0
		self.url1 = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term1)
		self.url2 = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term2)
		self.url3 = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term3)
		

	def run(self):
		response1 = requests.get(self.url1)
		response2 = requests.get(self.url2)
		response3 = requests.get(self.url3)
		soup1 = BeautifulSoup(response1.text,'html.parser')
		soup2 = BeautifulSoup(response2.text,'html.parser')
		soup3 = BeautifulSoup(response3.text,'html.parser')
	
		hr1 = soup1.find_all('div',class_ = 'st')
		hr2 = soup2.find_all('div',class_ = 'st')
		hr3 = soup3.find_all('div',class_ = 'st')

		hr1.extend(hr2)
		hr1.extend(hr3)
				

		for h in hr1:
			blob = TextBlob(h.get_text())
			self.sentiment += blob.sentiment.polarity / len(hr1)
			self.subjectivity += blob.sentiment.subjectivity / len(hr1)

a = Analysis(input())
a.run()
print('Topic :',a.term1, '\nSubjectivity :' , a.subjectivity, '\nSentiment:', a.sentiment)