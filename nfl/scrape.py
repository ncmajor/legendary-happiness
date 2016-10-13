import urllib2
from bs4 import BeautifulSoup
import pandas as pd

def requestSite(pos, url='https://sports.yahoo.com/nfl/stats/byposition?', \
	             year=None, tf='all',):
	""" Requests Yahoo Sports stats page for 
	a specific position. Position type must be 
	given as an argument. Default year is current year."""
	pos = str(pos)
	url +='pos=' + pos.upper()+ '&'
	if year != None:
		url +='year=season_' + str(year) + '&'
	tf = tf[0].upper()
	url +='timeframe=' + tf + '&'
	f = urllib2.urlopen(url)
	html = f.read()
	return html

def requestN(pos, year, url='https://sports.yahoo.com/nfl/stats/byposition?', \ 
			postseason=False, tf='All'):
	"""Returns the nth season or postseason, and any timeframe"""
	pos = str(pos)
	url +='pos=' + pos.upper() +'&'
	if postseason == False:
		url += 'year=season_' + str(year) + '&'
	else:
		url += 'year=postseason_' +str(year) + '&'
	tf = tf[0].upper()
	url += 'timeframe=' + tf + '&'
	f = urllib2.urlopen(url)
	html = f.read()
	f.close()
	return html

def nSeason(pos, year, postseason=False, tf='All'):
	html = requestN(pos, year, postseason, tf)
	dfs = pd.read_html
	df = dfs[-1]
	df = df.drop(0)
	df = df.drop()

def season2015(pos):
	#makes a dataframe from html data
	html = requestSite(pos, year=2015)
	dfs = pd.read_html(html)
	df = dfs[-1]
	df = df.drop(0)
	#df = df.rename(columns=df.ix[1])
	df = df.drop(1)
	return df

def season2016(pos):
	#makes a dataframe from html data
	html = requestSite(pos)
	dfs = pd.read_html(html)
	df = dfs[-1]
	df = df.drop(0)
	#df = df.rename(columns=df.ix[1])
	df = df.drop(1)
	return df

if __name__ == "__main__":
	df = season2015('rb')
	print df
	


