"""
Base Class Shortner
"""

import urllib2
import json

class BaseShortner( object ):

      API_URL = None

      def __init__(self, **kargs):

          import requests
          
          self.kargs = kargs

          self.requests = requests

      def _get(self, url, params = None):

          return self.requests.get(url, params = params, timeout = 0.5)

      def _get2(self, url, params = None):

          url = "http://api.bit.ly/shorten?longUrl=http://thinkhpp.ro/blog&login=thinkphp&apiKey=R_0cf8415f0c3f9fcfd867ce7613e43fc7&format=json"

          f = urllib2.urlopen( url )

          return json.loads( f.read() )

      def short(self, url):

          return url  

      def is_json(myjson):

          try:

            json_object = json.loads(myjson)

          except ValueError, e:

            return False

          return True


class BitlyShortner( BaseShortner ):

      API_URL = 'http://api.bit.ly'

      def __init__(self, **kargs):

          self.token = kargs.get('bitly_token') 

          super(BitlyShortner, self).__init__(**kargs)

      def short2(self, url):

          r = self._get2( url )

          for i in r:

            if i == 'results':

              ob = (r[i]) 

              for j in ob:

                  for k in ob[j]:

                      out = ob[j][k]

                      return 'http://bit.ly/'+out.encode('utf8')


      def short(self, url):

          shorten_url = '{0}{1}'.format(self.API_URL, '/shorten?')

          url = "http://api.bit.ly/shorten?longUrl=http://thinkhpp.ro/blog&login=thinkphp&apiKey=R_0cf8415f0c3f9fcfd867ce7613e43fc7&format=json"

          response = self._get( url )

          r = response.json()

          for i in r:

            if i == 'results':

              ob = (r[i]) 

              #print i, ' => ' ,r[i]

              for j in ob:

                  for k in ob[j]:

                      out = ob[j][k]

                      return 'http://bit.ly/'+out.encode('utf8')
              

ob = BitlyShortner(api_key = '')

print ob.short('http://thinkphp.ro/blog')      