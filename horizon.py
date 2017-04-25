#!/usr/bin/python
#This script assumes the earth is a perfect sphere, resulting in calculations within 1% of the actual result
import sys
earthRadius = 6371000 #in meters
#height = input ("Enter the height (in meters):")
height = int(sys.argv[1])
distance = (2*earthRadius*height+height*height)**.5
print int(distance)
