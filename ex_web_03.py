
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url:')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))

for v in range(count+1) :
	print(url)
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	lista = soup.find_all('a')
	url = lista[pos-1].get('href', None)

