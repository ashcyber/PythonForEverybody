'''
http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
'''
'''
Reference:

^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end

'''


#course2 bbbbbb

'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = dict()
for line in handle:
    if not line.startswith('From ') : continue
    line = line.split()
    time_of_day = line[-2].split(':')[0]
    time[time_of_day] = time.get(time_of_day,0) + 1

lst = sorted((v,k) for (v,k) in time.items())

for (k,v) in lst:
    print(k,v)

'''

#course3
#p1
'''
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+', line):
        print(line)
'''

#course3
#p2

'''
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[aeiou]+',x)
print(y)
'''


#assignment
'''
import re
hand = open('regex_sum_66354.txt')
numbers = []
for line in hand:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    numbers = numbers + num

total = 0
for num in numbers:
    total = total + int(num)
print(total)
'''

#course3
# decode is used to convert utf-8 to bytes which is str in python3
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('YYY')
for line in fhand:
    print(line.decode().strip())
'''
