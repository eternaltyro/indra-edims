#!/usr/bin/python

# From http://www.tutorialspoint.com/python/python_xml_processing.htm

from sys import argv, exit

#script, filename = argv


msgType = [ "Alert", "Update", "Cancelk", "Ack", "Error" ]
scope = [ "Public", "Private", "Restricted" ]
category = [ "Geo", "Met", "Safety", "Security", "Rescue", "Fire", "Health", "Env", "Transport", "Infra", "CBRNE", "Other" ]
responseType = [ "Shelter", "Evacuate", "Prepare", "Execute", "Avoid", "Monitor", "Assess", "AllClear", "None" ]
urgency = [ "Immediate", "Expected", "Future", "Past", "Unknown" ]
severity = [ "Extreme", "Severe", "Moderate", "Minor", "Unknown" ]
certainty = [ "Observed", "Likely", "Possible", "Unlikely", "Unknown" ]

def alertbegin ():
    print "What kind of crisis are you in?"
    shtf = raw_input('> ')
    if "file" in shtf:
        print "Enter filename: "
        cap_fn = raw_input('> ')
        cap_cache = open(cap_fn)
        print "File opened for read"
        cap_cache.close()
        print "file closed"
    else:
        alrt, response = alertGen(shtf)
        sendAlert(alrt, response)

def alertGen (alrt):
    if alrt == "Geo" or alrt == "Met" or alrt == "Fire":
        response = responseType[1]
        return alrt, response
    elif alrt == "Safety" or alrt == "Health" or alrt == "Env":
        response = responseType[0]
        return alrt, response
    elif alrt == "Security" or alrt == "Rescue" or alrt == "Other":
    	response = responseType[2]
        return alrt, response
    elif alrt == "CBRNE" or alrt == "Transport" or alrt == "Infra":
        response = responseType[6]
        return alrt, response
    else:
    	print "Invalid Alert Type, Re-enter"
        response = "NULL"
        exit (0)

def sendAlert (xyz, abc):
    print " ***** ALERT ***** "
    print "\n Alert: %s \n Response: %s \n" % (xyz, abc)


alertbegin()
