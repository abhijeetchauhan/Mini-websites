import webapp2
import os
import jinja2
from google.appengine.ext import db
import urllib2
from xml.dom import minidom

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape = True)

class Handler(webapp2.RequestHandler):
  def write(self,*a,**kw):
    self.response.out.write(*a,**kw)
  def render_str(self,template,**params):
    t=jinja_env.get_template(template)
    return t.render(params)
  def render(self,template,**kw):
    self.write(self.render_str(template,**kw))

#----------------------------------------- API -----------------------------------------------#
GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false"

def gmaps_img(points):
    URL=GMAPS_URL
    for point in points:
        URL = URL +"&markers="+str(point.lat)+","+str(point.lon)
    return URL


IP_URL="http://api.hostip.info/?ip="
def get_coords(ip):
  url=IP_URL+ip
  content = None
  try:
    content = urllib2.urlopen(url).read()
  except URLerror:
    return
  if content:
    #parse the xml and find the coordinates
    x = minidom.parseString(content)
    coords = x.getElementsByTagName('gml:coordinates')
    if  coords and coords[0].childNodes:
        lon,lat = coords[0].childNodes[0].nodeValue.split(',')
        return db.GeoPt(lat,lon)

       


class Art(db.Model):
  title=db.StringProperty(required = True)
  art=db.TextProperty(required = True)
  created=db.DateTimeProperty(auto_now_add = True)
  coords=db.GeoPtProperty()

class MainPage(Handler):
  def render_front(self,title="",art="",error=""):
    arts=db.GqlQuery("SELECT * FROM Art ORDER BY created DESC LIMIT 10")
    #prevents the running of multiple queries
    arts=list(arts)
    #find which arts has coordinates
    points=filter(None,(a.coords for a in arts))
    #if we have any arts coords make a image url
    image_url=None
    if points:
      image_url = gmaps_img(points)
    self.render('form.html',title=title,art=art,error=error,arts=arts,image_url=image_url)

  def get(self):
    self.render_front()
  def post(self):
    art=self.request.get("art")
    title=self.request.get("title")
    if art and title:
      a = Art(title=title,art=art)
      coords=get_coords(self.request.remote_addr)
      if coords:
        a.coords=coords

      a.put()
      self.redirect('/')
    else:
      error='We need both art and title'
      self.render_front(title,art,error)

app = webapp2.WSGIApplication([('/', MainPage)
              ], debug=True)
