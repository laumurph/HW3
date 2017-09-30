## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route("/artistform")
def artist_form():
	return render_template("artistform.html")

@app.route("/artistinfo")
def artist_info():	
	artist = request.args.get("artist")
	res = requests.get("https://itunes.apple.com/search?", params={'media': 'music', 'term': artist})
	return render_template("artist_info.html", objects=json.loads(res.text)['results'])

@app.route("/artistlinks")
def artist_links():
	return render_template("artist_links.html")

@app.route("/specific/song/<artist_name>")
def specific_artist(artist_name):
	print("*****************", artist_name)
	res = requests.get("https://itunes.apple.com/search?", params={'media': 'music', 'term': artist_name})
	print(json.loads(res.text))

	return render_template("specific_artist.html", results= json.loads(res.text)['results'])

if __name__ == '__main__':
    app.run(debug=True)
