import urllib
import urllib2
import json

class Google:

      ENDPOINT = 'https://ajax.googleapis.com/ajax/services/search/web?'

      API_KEY = 'B59F3913692A46D75ED39BA8F472DF267E24B611'

      def __init__(self, appid):

          self.appid = appid

      def search(self,**params):
 
          data = {}

          for k,v in params.items():

              data.update({k.replace('_','.'):v.replace(' ','+')})

          qs = urllib.urlencode(data)

          url = '%sv=1.0&userip=192.168.0.1&rsz=8&hl=en&start=0&%s' % (self.ENDPOINT, qs)

          f = urllib2.urlopen(url)

          return json.loads(f.read())

g = Google('none')

print g.search(q='Mootools')