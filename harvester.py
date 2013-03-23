from urlparse import urlparse
import urllib 
import json as simplejson
import sys
import socket
import time
import re

domain = sys.argv[1]
prefix = "site:"
domains = []
f = open( 'prefixes.txt', "r" )
prefixes = []
potentialdomains = []

# Create list from dictionary
for line in f:
    line = line.replace('\n', '')
    potentialdomains.append(line + '.' + domain)

# API Content
#url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBX66Vud5EPZI5Otrio7SOixbtePqNp9WI&cx=009303986479250505344:xvznns9nxi0&q=' + prefix + domain
url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBX66Vud5EPZI5Otrio7SOixbtePqNp9WI&cx=009303986479250505344:k7n4sohx3qo&q=' + prefix + domain


sr = urllib.urlopen(url)
json = simplejson.loads(sr.read())
results = json['items']

for i in results:
    link = i['link'].encode('ascii')
    url = urlparse(link)
    potentialdomains.append(url.hostname)

for i in potentialdomains:
    try:
        socket.gethostbyaddr(i)
    except:
        potentialdomains.remove(i)

print potentialdomains
