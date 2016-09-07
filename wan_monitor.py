import sys
from connection import *
from tcrules import *

upThreshold = 2  #no. of up pings to call iface as up
downThreshold = 5 # no. of down pings to call iface as down

db.connect()

con1 = Connection("eth0", "act",1,"192.168.1.1")
con2 = Connection("eth1","act",2,"8.8.8.8")

connectionList = [con1,con2]
activeConnectionList = []

for wan in connectionList:
	print "Status of %s is %d" % (wan.interfaceName,wan.status.state)
	if(wan.ping() != wan.status.state):  #state change detected in ping
		if(wan.status.state): # if iface was up and ping is down
			wan.increaseDownCount()
			print "Down count increased for %s to %d of %d" % (wan.interfaceName,wan.status.downCount,downThreshold)
			if(wan.status.downCount >= downThreshold):
				wan.changeState()
				wan.resetAllCount()
				print "stage changed to down for %s" % wan.interfaceName
					
			else:
				wan.resetUpCount()	
			

		else: #if iface was down and ping is live
			wan.increaseUpCount()
			print "Up count increased for %s to %d of %d" % (wan.interfaceName,wan.status.upCount,upThreshold)
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
	# create a list of currently active connections
	if (wan.status.state): 
		activeConnectionList.append(wan) 
# create a tcrules file for active connections and save in shorewall
TCRulesFile = TCrules("tcrules","/Users/rajath/dev/python/wan_monitor_env/wan_monitor")
TCRulesFile.writeFile(activeConnectionList)
TCrules.restartShorewall()
