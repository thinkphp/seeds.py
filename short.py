import urllib
import urllib2
import urlparse
import httplib
import json

BITLY_AUTH = 'login=thinkphp&api=R_0cf8415f0c3f9fcfd867ce7613e43fc7'

class URLShortner:

      services = {
          'api-ssl.bitly.com' : '/v3/shorten?login=thinkphp&apiKey=R_0cf8415f0c3f9fcfd867ce7613e43fc7&format=json&longUrl='
      }

      def query(self,url):

         for shortner in self.services.keys(): 

             conn = httplib.HTTPConnection(shortner)

             conn.request("GET",self.services[shortner] + urllib.quote(url))

             r1 = conn.getresponse()

             shorturl = r1.read().strip()

             if("Error" not in shorturl) and (urlparse.urlparse(shortner)[1] in shorturl):
                 return shorturl

                    

#ob = URLShortner()
#res = json.loads(ob.query('http://thinkphp.ro'))
#short = res['data']['url']
#print short


class URLExpander:
  # known shortening services
  shorteners = ['tr.im','is.gd','tinyurl.com','bitly.com','goo.gl']
  twofers = [u'\u272Adf.ws']
  # learned hosts
  learned = []
    
  def resolve(self, url, components):
    """ Try to resolve a single URL """
    c = httplib.HTTPConnection(components.netloc)
    c.request("GET", components.path)
    r = c.getresponse()
    print r.getheaders()
    l = r.getheader('Location')
    if l == None:
      return url # it might be impossible to resolve, so best leave it as is
    else:
      return l
  
  def query(self, url, recurse = True):
    """ Resolve a URL """
    components = urlparse.urlparse(url)
    print components
    # Check weird shortening services first
    if (components.netloc in self.twofers) and recurse:
      return self.query(self.resolve(url, components), False)
    # Check known shortening services first
    if components.netloc in self.shorteners:
      return self.resolve(url, components)
    # If we haven't seen this host before, ping it, just in case
    if components.netloc not in self.learned:
      ping = self.resolve(url, components)
      if ping != url:
        self.shorteners.append(components.netloc)
        self.learned.append(components.netloc)
        return ping
    # The original URL was OK
    return url

ob = URLExpander()
print ob.query("goo.gl/TYUyO")