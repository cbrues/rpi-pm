#!/usr/bin/python
#
# pm-reportemail.py
#
# Sends an email report to the configured email account.

# Import the neccesary librarys
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

PM_SUBJECT = 'Power monitor daily status report'
PM_TOSEND = '/home/powermonitor/power.log'
PM_AUTHFILE = '/home/powermonitor/emailauth'

with open( PM_AUTHFILE ) as authfile:
	PM_SENDER = authfile.readline().strip()
	PM_PASSWORD = authfile.readline().strip()
	PM_SENDTO = [ authfile.readline().strip() ]

# Construct the message
msg = MIMEMultipart()
msg['Subject'] = PM_SUBJECT
msg['From'] = PM_SENDER
msg['To'] = ", ".join( PM_SENDTO )

# Attache the file
msg.attach( MIMEText( open( PM_TOSEND , 'r' ).read() ) )

# Send the message
server = SMTP( 'smtp.gmail.com:587' )
server.starttls()
server.login( PM_SENDER , PM_PASSWORD )
server.sendmail( PM_SENDER , PM_SENDTO , msg.as_string() )
server.quit()

