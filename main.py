from flask import *
import pickle
import time
import os
import json

app = Flask(__name__, static_url_path = "")
items = pickle.load(open("dumps/items.pickle","rb"))
user_id = None
movie_id = None
@app.route("/")
def index():
	print "a"
	return render_template("moviepage_1.html")

@app.route("/set/user", methods = ["POST"])
def set_user():
	print "a"
	print request.form
	print "b"
	return "True"
	
@app.route("/set/movie", methods = ["POST"])
def set_movie():
	movie_id = request.form["id"]
	return "True"
	
@app.route("/get/movie_details")
def get_movie_details():
	print items[int(request.args["id"])]	
	item = dict(items[int(request.args["id"])])
	item["genre"] = list(item["genre"])
	movie_details = json.JSONEncoder().encode(item)
	return movie_details
if __name__ == "__main__":
	port = int(os.environ.get('PORT',1730))
	app.run( host = "127.0.0.1",port = port, debug = True)