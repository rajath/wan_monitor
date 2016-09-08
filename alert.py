import datetime
import os
class Alert:
	"""
		Class to define an email or sms Alert
	"""
	def __init__(self, alertMedium,alertTarget, interfaceName,alertType):
	      	self.alertMedium = alertMedium #email or sms or slack
	      	self.alertTarget = alertTarget #list of addresses or numbers
	      	self.alertType = alertType #up alert or down alert
		self.interfaceName = interfaceName #name of interfaceName


	def sendAlert(self):
		"""
			Sends alert to target through specified alertMedium
		"""
		if(self.alertMedium == "email"):
			#prepare email subj and body
			now = datetime.datetime.now()
			nowStringHuman =  datetime.datetime.strftime(now,"%Y-%m-%d %H:%M")
			print type(nowStringHuman)
			emailSubject = "Interface "+self.interfaceName+" "+self.alertType.upper()+" at "+nowStringHuman
			emailBody = "The interface "+self.interfaceName+" is now "+self.alertType
			osCommand = "echo  '"+emailBody+"' | mail -s  '"+emailSubject+"'  "+self.alertTarget
			#send email from linux senmail
			os.system(osCommand)