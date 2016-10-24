import pandas as pd
import handle_data as hd

def scorePlayers(pos, year='2016', tf='All', postseason=None):
	"""Turns raw data into fantasy points"""
	df = hd.cleanData(pos, year, tf, postseason)
	

def findPlayerVariance(pos, year='2016', postseason=None):
	"""Returns the variance of a player from his expected performance
	on a weekwise basis"""
	i = 1
	while i < 17:
		tf = 'Week' + str(i)
		try:
			cleanDataWeek()


if __name__ == "__main__":
	pass