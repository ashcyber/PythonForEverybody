import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

links = list()
links.append(url)


for i in range(count):
    curUrl = links[-1]
    print(curUrl)
    html = urllib.request.urlopen(curUrl).read()
    soup = BeautifulSoup(html, 'html.parser')
    link_tag = soup('a')[pos-1]
    links.append(link_tag['href'])
print(links[-1])
