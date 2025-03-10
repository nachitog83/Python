import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
print('Count:', len(lst))

suma = int()

for item in lst:
	suma += int(item.find('count').text)

print('Sum:', suma)