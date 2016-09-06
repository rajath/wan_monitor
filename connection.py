class Connection:
   'Class to define a WAN connection'
   empCount = 0

   def __init__(self, interfaceName, wanName,wanPriority,wanPingIP):
      self.wanName = wanName
      self.interfaceName = interfaceName
      self.wanPriority = wanPriority
      self.wanPingIP  = wanPingIP
      Conection.count += 1
      
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary