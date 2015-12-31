import webapp2
import os
import jinja2
import re
from google.appengine.ext import db

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
#-----------------------------------------------------Database Stuff----------------------------------------------#
class User(db.Model):
  name=db.StringProperty(required = True)
  email=db.StringProperty(required = True)
  gender=db.StringProperty(required = True)
  age=db.StringProperty(required = True)
  created=db.DateTimeProperty(auto_now_add = True)
  last_modified=db.DateTimeProperty(auto_now = True)
# -------------------------------------------------- First Page --------------------------------------------------#
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
AGE_RE = re.compile(r"^[0-9]+$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_name(name):
  return name and USER_RE.match(name)
def valid_age(age):
  return age and AGE_RE.match(age)
def valid_email(email):
  return email or EMAIL_RE.match(email)
def valid_gender(gender):
  if gender == '':
    return False
  return True

class MainPage(Handler):
  def get(self):
    self.render('index.html',male='male',female='female')
  def post(self):
    have_error=False
    self.name=self.request.get('name')
    self.email=self.request.get('email')
    self.age=self.request.get('age')
    self.gender=self.request.get('gender')
    params=dict(name = self.name,email = self.email,age=self.age,male='male',female='female')

    if not valid_name(self.name):
      params['errorName']="That's not a valid name"
      have_error=True

    if not valid_age(self.age):
      params['errorAge']="That's not a valid age"
      have_error=True

    if not valid_gender(self.gender):
      params['errorGender']="That's not a valid gender"
      have_error=True

    if not valid_email(self.email):
      params['errorEmail']="That's not a valid email"
      have_error=True
    if have_error:
      self.render('index.html',**params)
    else:
      a=User(name=self.name,email=self.email,age=self.age,gender=self.gender)
      a.put()
      x=str(a.key().id())
      self.redirect('/quiz/%s'% x)
#---------------------------------------------------Quiz Page------------------------------------------------------------#
class QuizPage(Handler):
  def get(self,post_id):
    x=User.get_by_id(int(post_id))
    if x:
      self.render('quiz.html')
  def post(self,post_id):
    x=User.get_by_id(int(post_id))
    answers=[1,2,3]
    score=0
    if x:
      for i in range (1,4):
        d=self.request.get(str(i))
        if str(answers[i-1]) == d:
          score = score+1
      self.write(x.name+' score is '+str(score))
app = webapp2.WSGIApplication([('/', MainPage),('/quiz/([0-9]+)',QuizPage)
              ], debug=True)
