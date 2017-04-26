#!/usr/bin/python
#This script assumes the earth is a perfect sphere, resulting in calculations within 1% of the actual result
import sys,getopt
try:
	opts, args = getopt.getopt(argv, "hm:i:", ["metric_height=","imperial_height="])
except getopt.GetoptError:
	usage_text = 'horizon.py -m <metric height> -i <imperial height>'
	print usage_text
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print usage_text 
	elif opt in ("-m", "--metric"):
		earthRadius = 6371000 #in meters
		height = int(arg)
		distance = (2*earthRadius*height+height*height)**.5
	elif opt in ("-i","--imperial"):
		earthRadius =20900000
		height = int(arg)
	print int(distance)
