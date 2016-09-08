import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 class Email:

	@staticmethod

	def sendEmail(fromaddr,toaddr)	
 

		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "SUBJECT OF THE MAIL"
		 
		body = "YOUR MESSAGE HERE"
		msg.attach(MIMEText(body, 'plain'))
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "YOUR PASSWORD")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()