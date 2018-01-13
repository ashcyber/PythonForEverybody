import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags =  soup.find_all("span", class_="comments")
for tag in tags:
    sum = sum + int(tag.get_text())
print(sum)
