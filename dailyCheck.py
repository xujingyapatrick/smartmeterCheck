import sendemail
import MySQLdb


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
				if cursorTime.fetchall()<checkTime:
					emailContent.append("!!! no incoming data for device "+str(smartmeter)+" for 2 hours!")
				elif rows[2]==NULL:
					emailContent.append("device "+str(smartmeter)+" data is NULL")
				else:
					emailContent.append("device "+str(smartmeter)+" is working")
	except:
		emailContent.add("Error: unable to fetch data")
#prepare for sending email
emailText=""
for txt in emailContent:
	emailText=emailText+"\n"+txt

sendemail.send(emailText)






