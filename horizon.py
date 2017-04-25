#!/usr/bin/python
#This script assumes the earth is a perfect sphere, resulting in calculations within 1% of the actual result
earthRadius = 6371000 #in meters
height = input ("Enter the height (in meters):")
distance = (2*earthRadius*height+height*height)**.5
print 'The distance to the horizon is approximately:', int(distance), 'meters'
