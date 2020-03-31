import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = input('Enter location: ')
print('Retrieving', url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
  js = json.loads(data)
except:
  js = None
  print('======================Error======================')

c = 0
s = 0

for comment in js['comments']:
  c += 1
  s += comment['count']

print('Count:',c)
print('Sum:',s)