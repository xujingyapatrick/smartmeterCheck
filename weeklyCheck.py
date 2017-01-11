import sendemail
import MySQLdb

#prepare for sending email
emailText="Localserver working status weekly report\n\n"

f=open("weeklyReport.txt")
while 1:
	line=f.readline()
	if not line:
		f.close()
		break
	emailText=emailText+line+'\n';
sendemail.send(emailText)
f=open("weeklyReport.txt",'w')
#f.write('\0')
f.close()







