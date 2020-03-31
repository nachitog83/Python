import re
hand = open('regex_sum_293194.txt')
total = int()

for ln in hand :
    if not re.search('[0-9]+', ln) : continue
    lst = re.findall('[0-9]+', ln)
    for c in range(len(lst)) :
        t = int(lst[c])
        total += t
print(total)        

