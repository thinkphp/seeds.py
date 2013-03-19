import urllib
import urllib2
import json

class Bing:

      ENDPOINT = 'http://api.bing.net/format.aspx'

      def __init__(self, appid, format='json'):

          self.appid = appid
          self.format = format

      def search(self,**params):
 
          self.ENDPOINT = self.ENDPOINT.replace('format',self.format)

          data = {}

          for k,v in params.items():

              data.update({k.replace('_','.'):v.replace(' ','+')})

          qs = urllib.urlencode(data).replace('%2B','+')

          url = '%s?Appid=%s&%s' % (self.ENDPOINT, self.appid, qs) 

          f = urllib2.urlopen(url)

          if self.format == 'json':
             return json.loads(f.read())