import pandas as pd 
import scrape


def cleanData(pos, year='2016', postseason=None):
	"""Returns dataframe with descriptive column names and no NaN columns"""
	tf = 'All'
	pos = pos.upper()
	if pos == 'QB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist = [3, 13, 19, 22, 25]
		for x in droplist:
			df = df.drop(x, axis=1)	
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games', 4:'QBRate', \
			                    5:'Completions', 6:'Attempts', 7:'PercentComp',\
			                    8:'PassingYds', 9:'PassYdsPG', 10:'PassYDsAvg',\
			                    11:'PassTDs',\
			                    12:'Interceptions', 14:'Rushes', 15:'RushingYDs',\
			                    16:'RushYdsPG', 17:'RushYdsAvg', 18:'RushTD',\
			                    20:'Sacked', 21:'YdsLost', 23:'Fumbles', 24:'FumLost'},\
			                    inplace=False)
		return df

	elif pos == 'RB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist= [3, 9, 19, 22]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team',2:'Games', 4:'Rushes',\
								5:'RushingYDs', 6:'RushYdsPG', 7:'RushYdsAvg', \
								8:'RushTD', 10:'Receptions', 11:'Targeted',\
								12:'RecYds', 13:'RecYdsPG', 14:'RecYdsAvg',\
								15:'LongestRec', 16:'YdsAfterCatch', \
								17:'RecFirstDowns', 18:'RecTD', \
								20:'Fumbles', 21:'FumLost'}, inplace=False)
		return df

	elif pos == 'WR':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist = [3, 13,19, 25,28]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games', 4:'Receptions',\
						5:'Targeted', 6:'RecYds', 7:'RecYdsPG',\
						8:'RecYdsAvg', 9:'LongestRec', 10:'YdsAfterCatch',\
						11:'RecFirstDowns', 12:'RecTD', 14:'KickReturn',\
						15:'KRYds', 16:'KRAvg', 17:'KRLong', 18:'KRTD',\
						20:'PuntReturns', 21:'PRYDS', 22:'PRAvg', 23:'PRLong',\
						24:'PRTD', 26:'Fumbles', 27:'FumLost'})
		return df

	elif pos == 'TE':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist= [3, 13, 19, 22]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games', 4:'Receptions',\
						5:'Targeted', 6:'RecYds', 7:'RecYdsPG',\
						8:'RecYdsAvg', 9:'LongestRec', 10:'YdsAfterCatch',\
						11:'RecFirstDowns', 12:'RecTD', 14:'Rushes',\
						15:'RushingYDs', 16:'RushYdsPG', 17:'RushYdsAvg', \
						18:'RushTD', 20:'Fumbles', 21:'FumLost'})
		return df

	elif pos == 'DE':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'DT':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'NT':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'LB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'CB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'S':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'K':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 13, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
					   4:'0-19', 5:'20-29', 6:'30-39', 7:'40-49',\
					   8:'50+', 9:'FGMade', 10:'FGAttempt', 11:'FGPct',\
					   12:'LongestFG', 14:'PA_Made', 15:'PA_Attempted',\
					   16:'PAPct', 18:'Points'})
		return df

	elif pos == 'P':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 13]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
					   4:'Punt', 5:'Yards', 6:'AvgPunt', 7:'Longest', 8:'In20',\
					   9:'In10', 10:'FairCatches', 11:'Touchbacks',\
					   12:'Block'})
		return df

	else:
		raise ValueError("That's not a valid position")	

def cleanDataWeek(pos, year, tf, postseason=None):
	"""Returns dataframe with descriptive column names and no NaN columns on 
	weekwise basis"""
	pos = pos.upper()
	if pos == 'QB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist = [3, 12, 18, 21, 24]
		for x in droplist:
			df = df.drop(x, axis=1)	
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games', 4:'QBRate', \
			                    5:'Completions', 6:'Attempts',\
			                    7:'PassingYds', 8:'PassYDsAvg', 9:"LongestPass",\
			                    10:'Interceptions', 11:'PassTDs',\
			                    13:'Rushes', 14:'RushingYDs',\
			                    15:'RushYdsAvg', 16:"LongestRush", 17:'RushTD',\
			                    19:'Sacked', 20:'YdsLost', 22:'Fumbles', 23:'FumLost'},\
			                    inplace=False)
		return df

	elif pos == 'RB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist= [3, 9, 19, 22]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team',2:'Games', 4:'Rushes',\
								5:'RushingYDs',6:'RushYdsAvg', 7:"LongestRush",\
								8:'RushTD', 10:'Receptions', 11:'Targeted',\
								12:'RecYds', 13:'YardsPerRec', 14:'RecYdsAvg',\
								15:'LongestRec', 16:'YdsAfterCatch', \
								17:'RecFirstDowns', 18:'RecTD', \
								20:'Fumbles', 21:'FumLost'}, inplace=False)
		return df

	elif pos == 'WR':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist = [3, 13,19, 25,28]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games', 4:'Receptions',\
						5:'Targeted', 6:'RecYds', 7:'RecYdsPG',\
						8:'RecYdsAvg', 9:'LongestRec', 10:'YdsAfterCatch',\
						11:'RecFirstDowns', 12:'RecTD', 14:'KickReturn',\
						15:'KRYds', 16:'KRAvg', 17:'KRLong', 18:'KRTD',\
						20:'PuntReturns', 21:'PRYDS', 22:'PRAvg', 23:'PRLong',\
						24:'PRTD', 26:'Fumbles', 27:'FumLost'})
		return df

	elif pos == 'TE':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist= [3, 13, 19, 22]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games', 4:'Receptions',\
						5:'Targeted', 6:'RecYds', 7:'RecYdsPG',\
						8:'RecYdsAvg', 9:'LongestRec', 10:'YdsAfterCatch',\
						11:'RecFirstDowns', 12:'RecTD', 14:'Rushes',\
						15:'RushingYDs', 16:'RushYdsPG', 17:'RushYdsAvg', \
						18:'RushTD', 20:'Fumbles', 21:'FumLost'})
		return df

	elif pos == 'DE':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'DT':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'NT':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'LB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'CB':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'S':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 7, 10, 14, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
						4:'TackleSolo', 5:'TackleAssist', 6:'TackleTotal',\
						8:'Sacks', 9:'YardsLost', 11:'Interceptions', \
						12:'InterceptionsYds', 13:'IntTD',\
						15:'DefTD', 16:'ForcedFumble', \
						17:'PassesDefensed', 18:'Safeties'})
		return df

	elif pos == 'K':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 13, 19]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
					   4:'0-19', 5:'20-29', 6:'30-39', 7:'40-49',\
					   8:'50+', 9:'FGMade', 10:'FGAttempt', 11:'FGPct',\
					   12:'LongestFG', 14:'PA_Made', 15:'PA_Attempted',\
					   16:'PAPct', 18:'Points'})
		return df

	elif pos == 'P':
		df = scrape.nSeason(pos, year, tf, postseason)
		droplist=[3, 13]
		for x in droplist:
			df = df.drop(x, axis=1)
		df = df.rename(columns={0:'Name', 1:'Team', 2:'Games',\
					   4:'Punt', 5:'Yards', 6:'AvgPunt', 7:'Longest', 8:'In20',\
					   9:'In10', 10:'FairCatches', 11:'Touchbacks',\
					   12:'Block'})
		return df

	else:
		raise ValueError("That's not a valid position")	


def findMean(df, col):
	df[col] = df[col].astype(float)
	return df[col].mean()

def findStandardDev(df, col):
	df[col] = df[col].astype(float)
	return df[col].std()

def findStats(pos):
	df15  = scrape.season2015(pos)
	df16 = scrape.season2016(pos)
	col_list = findColumns(pos)
	mean_list15 = []
	std_list15 = []
	mean_list16 = []
	std_list16 = []
	listy_list = [mean_list15, std_list15, mean_list16, std_list16]
	for col in col_list:
		mean_list15.append(findMean(df15,col))
		mean_list16.append(findMean(df16,col))
		std_list15.append(findStandardDev(df15,col))
		std_list16.append(findStandardDev(df16,col))
	return listy_list

def standardizeNames(df):
	"""For use on dataframe object containing NFL names.
	Removes uppercase, as well as suffixes in order to join two
	dataframes together."""
	df.Name = [x.replace(' ', '') for x in df.Name]
	df.Name = [x.replace('III', '') for x in df.Name]
	df.Name = [x.replace('.', '') for x in df.Name]
	df.Name = [x.replace("'", '') for x in df.Name]
	df.Name = [x.lower() for x in df.Name]

def salaryMerge(df, dfkcsv):
	"""Merges a postionwise dataframe with draftkings salary information"""
	standardizeNames(df)
	dfdk = pd.read_csv(dkcsv)
	standardizeNames(dfdk)
	df2 = pd.concat([dfdk['Name'], dfdk['Salary'], dfdk['AvgPointsPerGame']],\
					axis=1)
	df3 = pd.merge(df, df2, how='inner', on='Name')
	return df3

class OFFplayer(object):
	"""An offensive player object should represent a particular players value towards
	an overall lineup. Meaning the amount of points he might be expected to 
	contribute, as well as his salary."""
	def __init__(self, name, pos, team, salary, value):
		self.name = name
		self.team = team
		self.pos = pos
		self.salary = salary
		self.value = value

class DSTplayer(object):
	"""defensive players have no salary, and are a component of 
	a DSTline object which has salary and value"""
	def __init__(self, pos, stat):
		self.pos = pos
		self.stat = stat
	#def 	

class DSTline(object):
	"""Is a discrete element of a lineup, comparable to OFFplayer class"""
	def __init__(self, value, salary):
		self.value = value
		self.salary = salary



if __name__ == '__main__':
	print cleanDataWeek('QB', '2014', 'Week2')


	
	


	