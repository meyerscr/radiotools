#!/usr/bin/python
#This script approximates the distance a radio wave can travel when frequency and gain are known
#This is uses Friis transmission equation
import sys
wavelength = int(sys.argv[1])
transmit_gain =  double(sys.argv[2])
receive_gain = double(sys.argv[3])
transmit_power = double(sys.argv[4])
receive_power = double(sys.argv[5])
distance  = (frequency*10**(gain/20))/4*3.14159
print int(distance)
