from bs4 import BeautifulSoup
import requests
from word_parsing import tokenize, tag_tokens

def displayHeadlines(source, headlines):

	source = []
	count = 0
	for head in headlines:
		if count < 5:
			source.append(head.getText())
			count += 1
		else:
			break

	return source

def journalScrape(top_headlines):

	r1 = requests.get('https://www.thejournal.ie/irish')
	coverpage = r1.content

	soup1 = BeautifulSoup(coverpage, 'html5lib')
	headlines = soup1.find_all('div', class_='text span-5 last')

	complete_headlines = []

	for tag in headlines:
		atag = tag.find_all('h4', class_=None)
		for a in atag:
			text = a.find_all('a')
			headline = displayHeadlines("Journal", text)
			complete_headlines += headline

	top_headlines["Journal"] = complete_headlines[0:5]
	return top_headlines

def RTEScrape(top_headlines):

	r1 = requests.get('https://www.rte.ie/news')
	coverpage = r1.content

	soup1 = BeautifulSoup(coverpage, 'html5lib')
	headlines = soup1.find_all('span', class_='underline')

	headlines = displayHeadlines("RTE", headlines)
	top_headlines["RTE"] = headlines
	return top_headlines

def irishIndependantScrape(top_headlines):
	r1 = requests.get('https://www.independent.ie')
	coverpage = r1.content

	soup1 = BeautifulSoup(coverpage, 'html5lib')
	headlines = soup1.find_all('h3', class_='hx')

	headlines = displayHeadlines("Independant", headlines)
	top_headlines["Independant"] = headlines
	return top_headlines

def irishTimesScrape(top_headlines):
	r1 = requests.get('https://www.irishtimes.com/')
	coverpage = r1.content

	soup1 = BeautifulSoup(coverpage, 'html5lib')
	headlines = soup1.find_all('span', class_='tr-headline')

	headlines = displayHeadlines("Irish Times", headlines)
	top_headlines["Irish Times"] = headlines
	return top_headlines
