from flask import *
import pickle
#import time
import os
import json
import ranking_1

app = Flask(__name__, static_url_path = "")

items = pickle.load(open("dumps/items.pickle","rb"))
users = pickle.load(open("dumps/user.pickle","rb"))
user_id = None
movie_id = None
encoder = json.JSONEncoder()
@app.route("/")
def index():
	print "a"
	return render_template("moviepage_1.html")

@app.route("/set/user", methods = ["POST"])
def set_user():
	global user_id 
	user_id = int(request.form["id"])
	print "user_id",user_id
	return encoder.encode(users[user_id])
@app.route("/get/sets")
def get_sets():
	print user_id
	sets = ranking_1.ranking(user_id);
	print sets[1]
	return encoder.encode(sets)
if __name__ == "__main__":
	port = int(os.environ.get('PORT',1730))
	app.run( host = "127.0.0.1",port = port, debug = True)