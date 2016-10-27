import urllib2
import re
import xml.etree.ElementTree as ET

#Import file from website
u = urllib2.urlopen('https://node.tampagov.net/api/rss/police')
#Save new traffic data locally
localFile = open('newtrafficdata.xml', 'wb')
localFile.write(u.read())
localFile.close()
#Parse the xml file and define the root of the xml
tree = ET.parse('newtrafficdata.xml')
root = tree.getroot()
#Put new data into array, define a master list to merge new data with
newTraffic=[]
masterList=[]
#For loop to seach through xml for 'item' then get the time and address, and append to traffic array
for channel in root.iter('item'):
    time = channel.find('pubDate').text
    description = channel.find('description').text
    addressFilter = re.compile(r'Address:(.+?)<br />', flags=re.DOTALL)
    address = addressFilter.findall(description)
    newTraffic.append([time, address])

#verbose output of new data
#print(newTraffic)
#Append deletes previous data, so you can merge the new data with the master list
masterList = masterList + newTraffic
print(masterList)
