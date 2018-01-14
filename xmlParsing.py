import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving: ', url)
data=urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
print('count: ' , len(comments))
sum = 0
for comment in comments:
    sum = sum + int(comment.find('count').text)
print('sum: ', sum)
