#https://github.com/nsisodiya/Get-Twitter-Links/blob/master/GetTwitterLib.py
#https://github.com/kasun/python-tail/blob/master/tail.py
#http://the.taoofmac.com/space/blog/2009/08/10/2205

import urllib
import urllib2
import urlparse
import httplib
import json
import socket

API_KEY = 'AIzaSyBkOhgCG8LUdWy5FGTcXVf-UTfPhYHEz00'

class URLShortner:

      service = 'https://www.googleapis.com/urlshortener/v1/url?key=%s'

      def query(self,url):

          self.service = self.service % API_KEY

          print self.service

          params = urllib.urlencode({"longUrl": url})

          headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                     "Connection":"Keep-Alive",
                     "Cookie":"authed=1",
                     "Host":"goo.gl"}

          conn = httplib.HTTPSConnection('goo.gl')

          conn.request("POST", self.service, params, headers)
     
          response = conn.getresponse()

          print response.status, response.reason

      def expand(self,shortUrl):

          self.service = self.service % API_KEY         

          conn = httplib.HTTPSConnection('googleapis.com')

          conn.request("GET", self.service + '&shortUrl=' + shortUrl)
     
          response = conn.getresponse()

          print response.status, response.reason

          resp = json.loads(response.read())

          print resp['longUrl']

          

ob = URLShortner()
ob.query("http://docs.python.org/release/2.5.2/lib/httplib-examples.html") 
#ob.expand("http://goo.gl/RoCG6") 
