import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.htm')
        self.response.write(template.render())
		
application = webapp2.WSGIApplication([
                                       ('/',MainPage),
                                       ], debug=True)