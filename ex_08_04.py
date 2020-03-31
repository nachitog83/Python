fname = input("Enter file name: ")
fh = open(fname)
lst = list()
flst = list()
for line in fh:
    lst = line.split()
    for word in lst:
        if word in flst: continue
        flst.append(word)

flst.sort()
print(flst)
