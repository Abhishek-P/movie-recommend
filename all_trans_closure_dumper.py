# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:29:31 2016

@author: Abhishek P Taula
"""

import pickle
import time
import ranking_1
start_time = time.time()
ranked_sets = dict()
for i in range(943):
	print i
	ranked_sets[i+1] = ranking_1.ranking(i+1)

with open("dumps/ranked_sets.pickle","wb") as dump:
	pickle.dump(ranked_sets,dump)
print "Time:",time.time() - start_time
	