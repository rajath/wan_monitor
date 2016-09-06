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
from connection import Connection

upThreshold = 2  #no. of up pings to call iface as up
downThreshold = 5 # no. of down pings to call iface as down


con1 = Connection("eth0", "airtel",1,"192.168.1.1")
con2 = Connection("eth1","act",2,"192.168.1.1")

connectionList = [con1,con2]

for wan in connectionList:
	if(wan.ping() != wan.wanSettings[2]):  #state change detected in ping
		if(wan.wanSettings[2]): # if iface was up and ping is down
			wan.increaseDownCount()
			if(wan.wanSettings >= downThreshold):
				wan.changeState()
				wan.resetAllCount()
					
			else:
				wan.resetUpCount()	
			print True

		else: #if iface was down and ping is live
			wan.increaseUpCount()
			if(wan.wanSettings >= upThreshold):
				wan.changeState()
				wan.resetAllCount()
					
			else:
				wan.resetDownCount()	
			print True
	else:
		wan.resetAllCount()