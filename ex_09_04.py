name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
bigw = None
bigc = None

for line in handle :
    lst = line.split()
    if len(lst) < 3 or lst[0] != 'From' : continue
    counts[lst[1]] = counts.get(lst[1],0) + 1

for key,value in counts.items() :
    if bigw is None or value > bigc :
        bigw = key
        bigc = value
       
print(bigw, bigc)