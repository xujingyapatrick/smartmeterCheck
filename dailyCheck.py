import sendemail
import MySQLdb
from datetime import datetime;


#check configure file
def parseConfig():
	f=open("checkConfig.txt")
	f.readline()
	smartmeterList=f.readline()
	smartmeterList=smartmeterList.split(',')
	smartmeterList.remove('\n')
	return smartmeterList

##################
#daily work flow
##################

db=MySQLdb.connect("localhost","root","355itu11","localserveri3")
cursor=db.cursor()
smartmeterList=parseConfig()
subCommand1="select * from data_register_data where sm_id="
subCommand2=" order by timestamp desc limit 1;"
emailContent=[]
cursorTime=db.cursor()
cursorTime.execute("select now();")
#use checkTime to record now time
checkTime=cursorTime.fetchall()
print(checkTime)
for smartmeter in smartmeterList:
	SQL=subCommand1+smartmeter+subCommand2
	try:
		cursor.execute(SQL)
		results=cursor.fetchall()
		if len(results)<1:
			emailContent.append("no record is found for device: "+smartmeter)
		else:
			for rows in results:
				#use convertTime to add 2 hours to the selected record timestamp
				convertTime=r"select timestamp('"+str(rows[3])+r"','2:00:00');"
				cursorTime.execute(convertTime)
				print(cursorTime.fetchall())
				if cursorTime.fetchall()<checkTime:
					emailContent.append("!!! no incoming data for device "+str(smartmeter)+" for 2 hours!")
				elif rows[2]==NULL:
					emailContent.append("device "+str(smartmeter)+" data is NULL")
				else:
					emailContent.append("device "+str(smartmeter)+" is working")
	except:
		emailContent.add("Error: unable to fetch data")
#prepare for sending email
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

emailText=weekdays[datetime.now().weekday()]+" report:\n"
for txt in emailContent:
	emailText=emailText+txt+'\n'

f=open("weeklyReport.txt",'a')
f.write(emailText)
f.close()

sendemail.send(emailText)






