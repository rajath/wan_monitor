import os

class TCrules:
	"""
		Class to reperesent a tcrules file
	"""
	def __init__(self, fileName,filePath):
	      	self.fileName = fileName
	      	self.filePath = filePath
	
	def writeFile(self,wanList):
		"""
			Writes contents of object to the template file
		"""
		fileContents = []
		fileHeader = "#MARK           SOURCE          DEST            PROTO   PORT(S) CLIENT PORT(S)  USER    TEST"
		fileContents.append(fileHeader) #create static header
		for wan in wanList: #create the body of the file
			wanRow = str(wan.wanPriority)+":P         -        -"
			fileContents.append(wanRow)

		tcrulesFile = open(self.filePath+"/"+self.fileName, 'w')
		for item in fileContents: #write to file
			tcrulesFile.write("%s\n" % item)