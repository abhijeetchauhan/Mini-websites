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

class MainPage(Handler):
  def get(self):
    self.render('index.html')
  # def post(self):
  #   art=self.request.get("art")
  #   title=self.request.get("title")
  #   if art and title:
  #     a = Art(title=title,art=art)
  #     coords=get_coords(self.request.remote_addr)
  #     if coords:
  #       a.coords=coords

  #     a.put()
  #     self.redirect('/')
  #   else:
  #     error='We need both art and title'
  #     self.render_front(title,art,error)

app = webapp2.WSGIApplication([('/', MainPage)
              ], debug=True)
