# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:05:19 2016

@author: Abhishek P Taula
"""

import pickle
items = pickle.load(open("dumps/items.pickle","rb"))
avg_age = pickle.load(open("dumps/avg_age.pickle","rb"))
avg_rating = pickle.load(open("dumps/avg_rating.pickle","rb"))
no_of_males = pickle.load(open("dumps/no_of_males.pickle","rb"))
no_of_females = pickle.load(open("dumps/no_of_females.pickle","rb"))
print type(items)
for i in range(1682):
	items[i+1]["males"] = no_of_males[i]
	items[i+1]["females"] = no_of_females[i]
	items[i+1]["avg_rating"] = avg_rating[i]
	items[i+1]["avg_age"] = avg_age[i]

pickle.dump(items, open("dumps/items.pickle","wb"))
	
	