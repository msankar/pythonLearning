import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url: ')
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

sum = 0
commentList = tree.findall('comments/comment')
for commentItem in commentList :
    ct = commentItem.find('count').text
    sum = sum + int(ct)

print sum
