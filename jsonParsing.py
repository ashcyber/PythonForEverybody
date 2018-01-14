#
# #Assignment1 Extracting data from json
# import urllib.request, urllib.parse, urllib.error
# import json
# url = input('Enter url: ')
# inp = urllib.request.urlopen(url).read()
# infos = json.loads(inp)
# comments = infos['comments']
#
# total = 0
# for comment in comments:
#         total = total + int(comment['count'])
# print(total)

#Assignment2 using GeoJSON API

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)

print("place id: ", js['results'][0]['place_id'])
