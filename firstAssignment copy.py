text = "X-DSPAM-Confidence:    0.8475";

pos = text.find(".")
print pos

num = text[pos:]
print num

floatNum = float(num)
print floatNum
