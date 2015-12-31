import webapp2
from google.appengine.api import mail

class MainPage(webapp2.RequestHandler):  
    def get(self):
      self.response.out.write("<form method='post'><input type='text' name='email_address'><input type='submit'></form>")

    def post(self):
        user_address = self.request.get("email_address")

        if not mail.is_email_valid(user_address):
            # prompt user to enter a valid address
            self.response.out.write("<input type='text' name='email_address' value='email_address'>Enter a valid input")
        else:
            confirmation_url = MainPage(self.request)
            sender_address = "abhijeetinfinite@gmail.com"
            subject = "Confirm your registration"
            body = """
Thank you for creating an account! Please confirm your email address by
clicking on the link below:

%s
""" % confirmation_url

            mail.send_mail(sender_address, user_address, subject, body)
  
app = webapp2.WSGIApplication([('/', MainPage)
              ], debug=True)
