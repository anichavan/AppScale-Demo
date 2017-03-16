
from flask import Flask, render_template, request, url_for
import urllib
import json
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html', title='Home')


@app.route('/recipes',methods=['POST'])
def callapi():
	ingredients = request.form['ingredients']
	params = {"key" : "7b85bc581b1345b5982b15b839383a3f","q":ingredients,"sort":"r"}
	myURL = "http://food2fork.com/api/search?%s" % (urllib.urlencode(params)) 
	response = json.loads(urllib.urlopen(myURL).read())
	return render_template('showrecipes.html',count=response['count'],data=response['recipes'])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

if __name__ == "__main__":
    app.run()
