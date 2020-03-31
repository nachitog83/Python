name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

counts = dict()

for ln in handle :
    if ln.startswith('From ') : counts[ln[ln.find(':')-2:ln.find(':')]] = counts.get(ln[ln.find(':')-2:ln.find(':')],0) + 1

for v,k in sorted(counts.items()) : print(v, k)
    
