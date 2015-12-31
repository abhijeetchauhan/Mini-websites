import webapp2
from string import punctuation
import cgi

form="""
<html>
  <head>
    <title>rot13</title>
  </head>
  <body>
    <h1>Enter Some text to rot13</h1>
    <form method='post'>
      <textarea name='text' style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
        <input type="submit">
    </form>
  </body>
</html>
"""
def rot13(string):
  output=""
  for ch in string:
    if not ch.isspace() and ch not in punctuation:
      if ord(ch)<=ord('m') and ord(ch)>=ord('a') or ord(ch)<=ord('M') and ord(ch)>=ord('A'):
        output=output+chr(ord(ch)+13)
      else:
        output=output+chr(ord(ch)-13)
    else:
      output=output+ch
  return output
def escape_html(s):
  return cgi.escape(s,quote=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.write_form()
    def post(self):
          inpt=self.request.get('text')
          process=rot13(inpt)
          self.write_form(process)
    def write_form(self,text=""):
        self.response.out.write(form % {'text':escape_html(text)})

class ThanksHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('that is a valid day')
app = webapp2.WSGIApplication([('/', MainPage),
              ], debug=True)
