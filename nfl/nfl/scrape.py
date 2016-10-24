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

def requestN(pos, year, url, \
			tf='All', postseason=None):
	"""Returns the nth season or postseason, and any timeframe"""
	assert type(url) is str
	pos = str(pos)
	url += 'pos=' + pos.upper() +'&'
	if postseason == None:
		url += 'year=season_' + str(year) + '&'
	else:
		url += 'year=postseason_' +str(year) + '&'
	tf[0].upper()
	url += 'timeframe=' + tf + '&'
	f = urllib2.urlopen(url)
	html = f.read()
	f.close()
	print url
	return html

def nSeason(pos, year, tf='All',  postseason=None):
	url='https://sports.yahoo.com/nfl/stats/byposition?'
	html = requestN(pos, year, url, tf, postseason)
	dfs = pd.read_html(html)
	df = dfs[-1]
	df = df.drop(0)
	df = df.drop(1)
	return df

def season2015(pos):
	#makes a dataframe from html data
	html = requestSite(pos, year=2015)
	dfs = pd.read_html(html)
	df = dfs[-1]
	df = df.drop(0)
	#df = df.rename(columns=df.ix[1])
	df = df.drop(1)
	return df
	"season2015() is deprecated"

def season2016(pos):
	#makes a dataframe from html data
	html = requestSite(pos)
	dfs = pd.read_html(html)
	df = dfs[-1]
	df = df.drop(0)
	#df = df.rename(columns=df.ix[1])
	df = df.drop(1)
	return df
	print "season2016() is deprecated"

if __name__ == "__main__":
	
	df = nSeason('de', '2014')
	for x in range(26):
		print df[x]


