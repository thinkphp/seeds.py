"""
Base Class Shortner
"""

import urllib2
import json

class BaseShortner( object ):

      API_URL = None

      def __init__(self, **kargs):

          self.kargs = kargs

      def _get(self, url, params = None):

          url = "http://api.bit.ly/shorten?longUrl=http://thinkhpp.ro/blog&login=thinkphp&apiKey=R_0cf8415f0c3f9fcfd867ce7613e43fc7&format=json"

          f = urllib2.urlopen( url )

          return json.loads( f.read() )

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

          self.api_key = kargs.get('api_key') 

          super(BitlyShortner, self).__init__( **kargs )

      def short(self, url):

          r = self._get( url )

          for i in r:

            if i == 'results':

              ob = ( r[ i ] ) 

              for j in ob:

                  for k in ob[ j ]:

                      out = ob[ j ][ k ]

                      return 'http://bit.ly/'+out.encode('utf8')              

ob = BitlyShortner(api_key = 'your-api-key')
print ob.short('http://thinkphp.ro/blog')     