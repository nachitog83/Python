name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
    lst = line.split()
    if len(lst) < 3 or lst[0] != 'From' : continue
    host = lst[1][lst[1].find('@')+1:]
    counts[host] = counts.get(host,0) + 1

print(counts)        
