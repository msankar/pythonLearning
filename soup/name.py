import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
position = raw_input('Enter position - ')
count = raw_input('Enter count - ')
position = int(position)
count = int(count)

html = urllib.urlopen(url).read() 
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags 
i = 0

tags = soup('a')
while i < count :
    tag = tags[position - 1]
    url = tag.get('href', None)
    print url
    html = urllib.urlopen(url).read() 
    soup = BeautifulSoup(html)
    tags = soup('a')
    i = i+1