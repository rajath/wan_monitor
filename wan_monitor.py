import sys
from connection import *
from tcrules import *

PING_IP = "8.8.8.8"
TCRULES_PATH = "/etc/shorewall"
TCRULES_FILE = "tcrules"

upThreshold = 5  #no. of up pings to call iface as up
downThreshold = 2 # no. of down pings to call iface as down

db.connect()

#initialize all connections
con1 = Connection("p5p1", "ACT",1,PING_IP)
con2 = Connection("p2p1","ACT_BACKUP",2,PING_IP)
con3 = Connection("em1","SPECTRANET",3,PING_IP)
connectionList = [con1,con2,con3]
#initialize list for active connections
activeConnectionList = []
#flag to check if any interface changed state
statusChangeFlag = False



for wan in connectionList:
	print "Status of %s is %d" % (wan.interfaceName,wan.status.state)
	if(wan.ping() != wan.status.state):  #state change detected in ping
		if(wan.status.state): # if iface was up and ping is down
			wan.increaseDownCount()
			print "Down count increased for %s to %d of %d" % (wan.interfaceName,wan.status.downCount,downThreshold)
			if(wan.status.downCount >= downThreshold):
				wan.changeState()
				wan.resetAllCount()
				statusChangeFlag = True
				print "stage changed to down for %s" % wan.interfaceName
					
			else:
				wan.resetUpCount()	
			

		else: #if iface was down and ping is live
			wan.increaseUpCount()
			print "Up count increased for %s to %d of %d" % (wan.interfaceName,wan.status.upCount,upThreshold)
			if(wan.status.upCount >= upThreshold):
				wan.changeState()
				wan.resetAllCount()
				statusChangeFlag = True
				print "stage changed to up for %s" % wan.interfaceName	
			else:
				wan.resetDownCount()	
	else:
		wan.resetAllCount()

	wan.saveStatus(wan.status)
	# create a list of currently active connections
	if (wan.status.state): 
		activeConnectionList.append(wan) 
# create a tcrules file for active connections and save in shorewall
TCRulesFile = TCrules(TCRULES_FILE,TCRULES_PATH)
TCRulesFile.writeFile(activeConnectionList)
if statusChangeFlag:
	TCrules.restartShorewall()
