import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='patemeryfl', api_key='09kwa5ad0c')
import plotly.graph_objs as go
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
#Put new data into array
newTraffic=[]
#For loop to seach through xml for 'item' then get the time and address, and append to traffic array
for channel in root.iter('item'):
    time = channel.find('pubDate').text
    address = channel.find('description').text
    newTraffic.append([time, address])
    go.Heatmap() #Send data to heatmap for plotly
#print(newtraffic[0].find("address", "<"))
print(newTraffic)
#Append deletes previous data, so you can merge the new data with the maste rlist
masterList = masterList + newTraffic
#Sends new data to plotly
py.iplot(data, filename='traffic-heatmap')
