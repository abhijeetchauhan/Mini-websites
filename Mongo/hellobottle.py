import bottle

@bottle.route('/')
def home_page():
  return "hello world\n"

@bottle.route('/testpage')
def test_page():
  return "this is test page"

bottle.debug(True)
bottle.run(host="localhost",port=8080)