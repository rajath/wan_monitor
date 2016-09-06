from models import *
class Connection:
   'Class to define a WAN connection'
   empCount = 0

   def __init__(self, interfaceName, wanName,wanPriority,wanPingIP):
      self.wanName = wanName
      self.interfaceName = interfaceName
      self.wanPriority = wanPriority
      self.wanPingIP  = wanPingIP
      self.wanSettings = self.fetchSettings()

      
   def fetchSettings(self):
      " Returns up count, down count, state"
      settings = [0,0,True]
      return settings

   def ping(self):
      """ 
            pings through a specific interface to check status
      """
      return True

   def changeState(self):
      """
            toggles state of interface
      """
      self.wanSettings[2] = not self.wanSettings[2]

   def increaseUpCount(self):
      """
            increase up counter by one
      """
      self.wanSettings[0] += 1

   def increaseDownCount(self):
      """
            increase down counter by one
      """
      self.wanSettings[1] += 1
       
   def resetUpCount(self):
      """
            resets up counter for the interface
      """
      self.wanSettings[0] = 0

   def resetDownCount(self):
      """
            resets down counter for the interface
      """
      self.wanSettings[1] = 0

   def resetAllCount(self):
      """
            resets down counter for the interface
      """
      self.resetDownCount()
      self.resetUpCount()
