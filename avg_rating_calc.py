# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:07:54 2016

@author: Abhishek P Taula
"""

import pickle
user_vs_movie = pickle.load(open("dumps/user_vs_movie.pickle","rb"))
avg_rating = [0 for i in range(1682)]
no_of_males = pickle.load(open("dumps/no_of_males.pickle","rb"))
no_of_females = pickle.load(open("dumps/no_of_females.pickle","rb"))
for user in user_vs_movie:
	for i in range(1682):
		avg_rating[i] += user[i]

for i in range(1682):
	avg_rating[i] = float(avg_rating[i])/(no_of_males[i] + no_of_females[i])

for i in range(1682):
	print avg_rating[i]
with open("dumps/avg_rating.pickle","wb") as dump:
	pickle.dump(avg_rating,dump)	