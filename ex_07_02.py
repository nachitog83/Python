# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print(line.rstrip())
    count += 1
    tot += float(line[line.find(':')+1:])
#print(tot)
#print(count)
print('Average spam confidence:',tot/count)
