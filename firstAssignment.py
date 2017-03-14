


fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
hourDict = dict()

for line in fh :
	line = line.rstrip()
	if line.startswith('From ') :
		words = line.split()
		hour = (words[5].split(":"))[0]
		hourDict[hour] = hourDict.get(hour,0) + 1

tempList = list()
for hour, count in hourDict.items() :
	tempList.append((hour, count))
	
tempList.sort()
print tempList
	
		
	#	senderDict[sender] = senderDict.get(sender,0) + 1

