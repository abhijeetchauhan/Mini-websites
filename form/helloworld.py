import webapp2
import cgi

form="""
<form method="post">
	Whats your Birthday?
	<br>
	<label>Month
	<input type='text' name='month' value='%(month)s'>
	</label>
	<label>Day
	<input type='text' name='day' value='%(day)s'>
	</label>
	<label>Year
	<input type='text' name='year' value='%(year)s'>
	</label>
	<div style="color:red">%(error)s<div>
	<br>
	<br>
	<input type="submit">
<form>
"""
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    for mon in months:
        if mon.upper() == month.upper():
            return month[0].upper()+month[1:].lower()
    return None
def valid_day(day):
    if day.isdigit():
        if int(day)>=1 and int(day)<=31:
            return int(day)
    return None
def valid_year(year):
    if year.isdigit():
        no=int(year)
        if no>=1900 and no<=2020:
            return no
    return None
def escape_html(s):
	return cgi.escape(s,quote=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.write_form()
    def post(self):
    	user_month=(self.request.get('month'))
    	user_day=(self.request.get('day'))
    	user_year=(self.request.get('year'))
    	month=valid_month(user_month)
    	year=valid_year(user_year)
    	day=valid_day(user_day)
    	if not (year and day and month):
    		self.write_form('that is not right my friend',user_month,user_day,user_year)
    	else:
    		self.redirect('/thanks')
    def write_form(self,error="",month="",day="",year=""):
		self.response.out.write(form % {'error':error,'month':escape_html(month),'day':escape_html(day),'year':escape_html(year)})

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('that is a valid day')
app = webapp2.WSGIApplication([('/', MainPage),('/thanks',ThanksHandler)
   						], debug=True)
