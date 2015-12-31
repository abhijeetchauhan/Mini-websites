import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('<h1>test app engine</h1>')


app=webapp2.WSGIApplication([
	('/'),MainPage],debug=True)
