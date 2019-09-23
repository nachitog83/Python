fhand = open('mbox-short.txt')
inp = fhand.read()
print(inp[:20])
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
