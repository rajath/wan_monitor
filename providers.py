import os


class Providers:
	"""
		Class to reperesent a shorewall providers file
	"""
	def __init__(self, fileName,filePath):
	      	self.fileName = fileName
	      	self.filePath = filePath
	
	def writeFile(self,wanList):
		"""
			Writes contents of object to the template file
		"""
		fileContents = []
		fileHeader = "#NAME 	NUMBER 	MARK 		DUPLICATE 	INTERFACE 		GATEWAY      	OPTIONS          COPY"
		fileContents.append(fileHeader) #create static header
		for wan in wanList: #create the body of the file
			wanRow = wan.wanName+" "+str(wan.wanPriority)+" "+str(wan.wanPriority)+" main  $INT_WAN"+str(wan.wanPriority)+" "+"$WAN"+str(wan.wanPriority)+"_GTWY   track,balance  $INT_LAN"
			fileContents.append(wanRow)

		providersFile = open(self.filePath+"/"+self.fileName, 'w')
		for item in fileContents: #write to file
			providersFile.write("%s\n" % item)
