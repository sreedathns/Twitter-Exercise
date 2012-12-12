import webapp2
import urllib
import json

class MainPage(webapp2.RequestHandler):
  def get(self):
       	self.response.headers['Content-Type'] = 'text/plain'
       	count = 0
       	url = urllib.urlopen("https://api.twitter.com/1/statuses/user_timeline.json?inc lude_entities=true&include_rts=true&screen_name=pramode_ce&count=50")	
       	r = url.read()	
       	dict = json.loads(r)
   	for e in dict:
		if e["text"][0] != "R" and count<10: 
			count = count + 1 		
      			self.response.write(e["text"])
			self.response.write("\n")

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
