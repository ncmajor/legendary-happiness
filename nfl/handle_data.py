import pandas as pd 
from scrape import yahoo

def mergeFrames(pos):
	"""
	Merges the dataframes returned by 
	season2015 and season2016. Takes
	position argument and the column names
	to be summed."""
	df15 = yahoo.season2015(pos)
	df16 = yahoo.season2016(pos)
	df = pd.merge(df15, df16, how='right', on=['Name', 'Name'])
	return df


def findColumns(pos):
	pos = pos.upper()
	if pos == 'QB':
		col_list = [2,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,21,23,24] 
		return col_list
	elif pos == 'RB':
		col_list = [2,4,5,6,7,8,10,11,12,13,14,15,16,17,18,20,21]
		return col_list
	elif pos == 'WR':
		col_list = [2,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,21,22,\
					23,24,26,27]
		return col_list		
	elif pos == 'TE':
		col_list = [2,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21]
		return col_list
	elif pos == 'DE':
		col_list = [2,4,5,6,8,9,11,12,13,15,16,17,18]
		return col_list
	elif pos == 'DT':
		col_list = [2,4,5,6,8,9,11,12,13,15,16,17,18]
		return col_list
	elif pos == 'NT':
		col_list = [2,4,5,6,8,9,11,12,13,15,16,17,18]
		return col_list
	elif pos == 'LB':
		col_list = [2,4,5,6,8,9,11,12,13,15,16,17,18]
		return col_list
	elif pos == 'CB':
		col_list = [2,4,5,6,8,9,11,12,13,15,16,17,18]
		return col_list
	elif pos == 'S':
		col_list = [2,4,5,6,8,9,11,12,13,15,16,17,18]
		return col_list
	elif pos == 'K':
		col_list = [2,4,5,6,7,8,9,10,11,12,14,15,16,18]
		return col_list
	elif pos == 'P':
		col_list = [2,4,5,6,7,8,9,10,11,12]
		return col_list
	else:
		raise ValueError("That's not a valid position")	

def findMean(df, col):
	df[col] = df[col].astype(float)
	return df[col].mean()

def findStandardDev(df, col):
	df[col] = df[col].astype(float)
	return df[col].std()

def findStats(pos):
	df15  = yahoo.season2015(pos)
	df16 = yahoo.season2016(pos)
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
	df.Name = [x.lower() for x in df.Name]

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
	print findStats('rb')

	