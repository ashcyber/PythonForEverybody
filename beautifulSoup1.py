import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = 'http://py4e-data.dr-chuck.net/comments_66356.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


#parse all the a tags

sum = 0
tags =  soup.find_all("span", class_="comments")
for tag in tags:
    sum = sum + int(tag.get_text())
print(sum)
