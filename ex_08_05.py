
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    ln = line.split()   
    if len(ln) < 3 or ln[0] != 'From' : continue
    count += 1
    print(ln[1])
print("There were", count, "lines in the file with From as the first word")