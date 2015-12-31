import webapp2
MAIN_PAGE_HTML = """\
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Roux Academy App</title>
<style>
body {
	background-color: #999999;
	margin: 0;
	padding: 0;
}
#outerWrapper {
	width: 800px;
	margin: 0 auto;
	background-color: #fff;
}
header {
	background: #000000;
	height: 80px;
	padding-top: 15px;
	padding-left: 15px;
	color: white;
}
</style>
</head>

<body>
<div id="outerWrapper">
  <header>
    <p id="raTitle">Roux Academy<br>
      Art &bull; Media &bull; Design</p>
  </header>
  <article id="main"> </article>
</div>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)
        
application = webapp2.WSGIApplication([
                                       ('/',MainPage),
                                       ], debug=True)
    