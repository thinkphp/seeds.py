import re
import sys
import urllib2
import datetime

if len(sys.argv) != 2:
       print "Usage: python google-stats http://yoursite.com"
       sys.exit() 

domain = sys.argv[1]

url = "http://www.google.com/search?q=site:%s" % domain

headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

req = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(req).read()

now = datetime.datetime.now()

count = re.search(r'(About)? ?([\d,]+) results', response).groups()

if count[0] == None:
    print "%s\t %s hits" % (now,count[1])
else:
    print "%s\t %s %s hits" % (now, count[0],count[1])