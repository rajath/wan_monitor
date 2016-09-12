import os

class TCRules:
	"""
		Class to reperesent a tcrules file
	"""
	def __init__(self, fileName,filePath):
	      	self.fileName = fileName
	      	self.filePath = filePath
	
	def writeFile(self,activeWanList,fullWanList):
		"""
			Writes contents of object to the template file
		"""
		fileContents = []
		fileHeader = "#MARK           SOURCE          DEST            PROTO   PORT(S) CLIENT PORT(S)  USER    TEST"
		fileContents.append(fileHeader) #create static header
		if len(activeWanList) != len(fullWanList):
			for wan in activeWanList: #create the body of the file
				wanRow = str(wan.wanPriority)+":P         -        -"
				fileContents.append(wanRow)

		tcrulesFile = open(self.filePath+"/"+self.fileName, 'w')
		for item in fileContents: #write to file
			tcrulesFile.write("%s\n" % item)

