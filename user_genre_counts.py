# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:51:30 2016

@author: Abhishek P Taula
"""

import time
import pickle

start_time = time.time()

items = pickle.load(open("dumps/items.pickle", "rb"))
user_movies_list = pickle.load(open("dumps/user_movies_list.pickle", "rb"))
user = pickle.load(open("dumps/user.pickle", "rb"))
user_vs_movie = pickle.load(open("dumps/user_vs_movie.pickle", "rb"))
for i in range(len(user_movies_list)):
    user[i + 1]["genre_count"] = dict()
    user[i + 1]["genre_score"] = dict()
    for j in user_movies_list[i]:
        genre = items[j]["genre"]
        for k in genre:
            if not k in user[i + 1]["genre_count"]:
                user[i + 1]["genre_count"][k] = 0
                user[i + 1]["genre_score"][k] = 0
            user[i + 1]["genre_count"][k] += 1
            user[i + 1]["genre_score"][k] += user_vs_movie[i][j - 1]
with open("dumps/user.pickle", "wb") as dump:
    pickle.dump(user, dump)
print len(user)
print user[1]["genre_score"]
print "Time:", time.time() - start_time
