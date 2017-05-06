#!/usr/bin/python
#This script assumes the earth is a perfect sphere, resulting in calculations within 1% of the actual result
import sys,getopt
try:
	optlist, args = getopt.getopt(sys.argv, "hi:", ["help", "imperial_height="])
	usage_text = 'horizon.py -h help [-i <imperial height]>'
except:
	print ("Did not recognize first option: {}", optlist[0][0]).format()
	sys.exit(3)
def setup_args(options, arguments):
	height = int(arguments[1])
	if (len(arguments)>2):
		print "Please pass only one argument."
		print usage_text
		sys.exit(2)
	earthRadius = 6371000 #in meters
	#if (options[1] == 'i'):
	earthRadius =20900000
	distance = (2*earthRadius*height+height*height)**.5
	print int(distance)
'''
This truncates any digits beyond the decimal. Real world calculations are far less accurate than this and should effect your results.
'''
setup_args(optlist, args)

