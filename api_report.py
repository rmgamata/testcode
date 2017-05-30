import os
from decimal import *
from datetime import datetime

gen_report = open("report.html", "a")
gen_report.write("<html><table align='center' border='1' width='80%'> </table><center>  <h3>API</h3></center>")
gen_report.write("<br/><table border='1' align='center' width='35%'><tr><td><h3>API</h3></td></tr></table>")
gen_report.write("<table border='1' align='center' width='35%'> <tr><td align='center' bgcolor='#c2c4c6' width='10%'> <b>Test Case</b> </td> <td align='center' bgcolor='#c2c4c6' width='60%'> <b>API </b></td>""<td align='center' bgcolor='#c2c4c6' width='20%'> <b>Pass/Fail </b></td></tr>")

passed = 0
failed = 0
gettestcases = set()
jtl = open("HTTPRequest.jtl", "r")
for line in jtl:
	if "lb" in line:
		line = line.replace('</httpSample>','').strip()
		gettestcases.add(line)
		
print '\n'.join(gettestcases)
testcases = len(gettestcases)

y = 1
for results in gettestcases:		
	if ('rc="200"' in results) and ('rm="OK"' in results):
		endvalue = results.find("lb=") 
		endvalue2 = results.find("rc")
		strtvalue = results.rfind('', 0, endvalue)
		strtvalue2 = results.rfind('', 0, endvalue2)
		getapi = results[strtvalue:strtvalue2].replace('lb=','').replace('"','')
		print "TEST CASE:", y,   "   ", getapi,  "Passed"
		getapi = str(getapi)
		y = str(y)
		gen_report.write("<tr><td align='center'>" + y + "</td><td>" + getapi + "</td> <td bgcolor='#99e26f'>Passed </td></tr>")
		passed+=1
		y = int(y)
		y+=1
	else:
		endvalue = results.find("lb=") 
		endvalue2 = results.find("rc")
		strtvalue = results.rfind('', 0, endvalue)
		strtvalue2 = results.rfind('', 0, endvalue2)
		getapi = results[strtvalue:strtvalue2].replace('lb=','').replace('"','')
		print "TEST CASE:", y,   "   ", getapi,  "Failed"
		getapi = str(getapi)
		y = str(y)
		gen_report.write("<tr><td align='center'>" + y + "</td><td>" + getapi + "</td> <td bgcolor='#e06745'>Failed </td></tr>")
		failed+=1
		y = int(y)
		y+=1
		
print "Passed: ", passed
print "Failed: ", failed
getcontext().prec = 3
percentage = Decimal(passed) / Decimal(testcases) * 100
totalper = str(percentage) + '%'
gen_report.write("</table><table align='center'> <tr><td><h3>Passed: " + totalper + "</h3></td></tr> </table>")

#api_result------------------------------------------------------------------------------==========================
api_result = open("api_result.html","a")
api_result.write("<center><h1>Build Acceptance Test</h1> <h3>API</h3></center>")
api_result.write("<br/> <table border='1' width='70%' align='center' width='35%'> <tr><td align='center' bgcolor='#c2c4c6' width='10%'> <b>Test Case</b> </td> <td align='center' bgcolor='#c2c4c6' width='40%'> <b>API </b></td> <td align='center' bgcolor='#c2c4c6'><b>Response Code</td>  <td align='center' bgcolor='#c2c4c6'><b>Response Message</td> <td align='center' bgcolor='#c2c4c6' width='20%'> <b>Result</b></td></tr>")


cc = 1
for extractor in gettestcases:
	endvalue_rc = extractor.find("rc=") 
	endvalue2_rc = extractor.find("rm")
	strtvalue_rc = extractor.rfind('', 0, endvalue_rc)
	strtvalue2_rc = extractor.rfind('', 0, endvalue2_rc)
	get_rc = extractor[strtvalue_rc:strtvalue2_rc].replace('rc=','').replace('"',' ').strip()
	print get_rc

	endvalue_rm = extractor.find("rm=") 
	endvalue2_rm = extractor.find("tn")
	strtvalue_rm = extractor.rfind('', 0, endvalue_rm)
	strtvalue2_rm = extractor.rfind('', 0, endvalue2_rm)
	get_rm = extractor[strtvalue_rm:strtvalue2_rm].replace('rm=','').replace('"',' ').strip()
	print get_rm

	endvalue_lb = extractor.find("lb=") 
	endvalue2_lb = extractor.find("rc")
	strtvalue_lb = extractor.rfind('', 0, endvalue_lb)
	strtvalue2_lb = extractor.rfind('', 0, endvalue2_lb)
	get_lb = extractor[strtvalue_lb:strtvalue2_lb].replace('lb=','').replace('"',' ').strip()
	print get_lb

	if ('rc="200"' in extractor) and ('rm="OK"' in extractor):
		cc = str(cc)
		api_result.write("<tr><td align='center'>" + cc + "</td><td>" + get_lb + "</td> <td>" + get_rc + "</td> <td>" + get_rm + "</td> <td bgcolor='#99e26f'>Passed </td></tr>")
		cc = int(cc)
		cc+=1
	else:
		cc = str(cc)
		api_result.write("<tr><td align='center'>" + cc + "</td><td>" + get_lb + "</td> <td>" + get_rc + "</td> <td>" + get_rm + "</td> <td bgcolor='#e06745'>Failed </td></tr>")
		cc = int(cc)
		cc+=1
#api_result------------------------------------------------------------------------------=============================




endtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')#time
opentime = open("writetime.txt", "r")
for gettime in opentime:
	if "Start Time" in gettime:
		starttime = gettime[12:].strip()
gen_report.write("<html><table align='center' border='1' width='80%'> </table>")
gen_report.write("<center><h2>Test Info</h2></center><table align='center' border='1' width='35%'> <tr><td> <b>Start Time:</b></td> <td width='70%'>" + starttime +  "</td></tr>"
		 "<tr><td><b>End Time:</b></td> <td>" + endtime + "</td></tr>"
		 "<tr><td> <b>Log File:</b></td><td>report.html</td></tr> </table>")
