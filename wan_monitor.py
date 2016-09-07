import traceback
#import pyaudio
import datetime
import time
import sys
import numpy as np
import os
import datetime as dt
import csv as csv
import glob as glob
from conn_models import *
from connection import Connection

upThreshold = 2  #no. of up pings to call iface as up
downThreshold = 5 # no. of down pings to call iface as down

db.connect()

con1 = Connection("eth0", "airtel",1,"192.168.1.1")
con2 = Connection("eth1","act",2,"192.168.1.1")

connectionList = [con1,con2]

for wan in connectionList:
	print "Status of %s is %d" % (wan.interfaceName,wan.status.state)
	if(wan.ping() != wan.status.state):  #state change detected in ping
		if(wan.status.state): # if iface was up and ping is down
			wan.increaseDownCount()
			print "Down count increased for %s to %d" % (wan.interfaceName,wan.status.downCount)
			if(wan.status.downCount >= downThreshold):
				wan.changeState()
				wan.resetAllCount()
				print "stage changed to down for %s" % wan.interfaceName
					
			else:
				wan.resetUpCount()	
			

		else: #if iface was down and ping is live
			wan.increaseUpCount()
			print "Up count increased for %s to %d" % (wan.interfaceName,wan.status.upCount)
			if(wan.status.upCount >= upThreshold):
				wan.changeState()
				wan.resetAllCount()
				print "stage changed to up for %s" % wan.interfaceName	
			else:
				wan.resetDownCount()	
			print True
	else:
		wan.resetAllCount()

	wan.saveStatus(wan.status)