import webapp2
import os
import jinja2
from google.appengine.ext import db
#---------------------------------- Jinja template Stuff ------------------------------------------------------------#
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape = True)


#-------------------------------------------- Class Handler ---------------------------------------------------------#
class Handler(webapp2.RequestHandler):
  def write(self,*a,**kw):
    self.response.out.write(*a,**kw)
  def render_str(self,template,**params):
    t=jinja_env.get_template(template)
    return t.render(params)
  def render(self,template,**kw):
    self.write(self.render_str(template,**kw))
 
#------------------------------------------------ Main Page ----------------------------------------------------------------#
class MainPage(Handler):
  def get(self):
    blogs=db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC limit 10")
    if self.format == 'html':
      if self.user:
        self.render('miniblog.html',blogs=blogs,log='Logout',page='/logout')
      else:
        self.render('miniblog.html',blogs=blogs,log='Login',page='/login')
    else:
      entry={}
      entries=[]
      for blog in blogs:
        entry["subject"]=blog.subject
        entry["content"]=blog.content
        entries.append(entry.copy())
      return self.render_json(entries)


  
app = webapp2.WSGIApplication([('/(?:\.json)?', MainPage)
              ], debug=True)
