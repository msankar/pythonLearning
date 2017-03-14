import re

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_286199.txt"

fh = open(fname)
sum = 0

for line in fh :
	line = line.rstrip()
	numList = re.findall('[0-9]+', line)
	if len(numList) < 1: continue
	for num in numList :
		sum += int(num)

print sum
	
		

