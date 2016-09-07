from conn_models import *
import os
import subprocess as sub

class ConnectionException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg



class Connection:
   'Class to define a WAN connection'
   empCount = 0

   def __init__(self, interfaceName, wanName,wanPriority,wanPingIP):
      self.wanName = wanName
      self.interfaceName = interfaceName
      self.wanPriority = wanPriority
      self.wanPingIP  = wanPingIP
      self.status = self.fetchStatus(interfaceName) #object

      
   def fetchStatus(self,interfaceName):
      " Returns up count, down count, state"

      try:
         settings = wanStatus.get(wanStatus.interfaceName == interfaceName)
      except:
         print "Cannot fetch settings from database for %s" % interfaceName
      else:
         return settings

   def ping(self):
      """ 
            pings through a specific interface to check status
      """
      FNULL = open(os.devnull,'w')
      result = not sub.call(['ping', '-q', '-c 1', '-W 1', self.wanPingIP],stdout=FNULL,stderr=sub.STDOUT)
      return result 

   def changeState(self):
      """
            toggles state of interface
      """
      self.status.state = not self.status.state 

   def increaseUpCount(self):
      """
            increase up counter by one
      """
      self.status.upCount += 1

   def increaseDownCount(self):
      """
            increase down counter by one
      """
      self.status.downCount += 1
       
   def resetUpCount(self):
      """
            resets up counter for the interface
      """
      self.status.upCount = 0

   def resetDownCount(self):
      """
            resets down counter for the interface
      """
      self.status.downCount = 0

   def resetAllCount(self):
      """
            resets down counter for the interface
      """
      self.resetDownCount()
      self.resetUpCount()

   def saveStatus(self,currentStatus):
      """
         Saves settings to database
      """
      status = wanStatus.get(wanStatus.interfaceName == self.interfaceName)
      status = currentStatus
      status.save()
      #q = wanStatus.update(status).where(wanStatus.interfaceName == interfaceName)
      #q.execute()
     
