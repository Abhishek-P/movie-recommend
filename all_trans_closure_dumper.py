# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:29:31 2016

@author: Abhishek P Taula
"""

import trans_clos
import pickle
import time
start_time = time.time()
all_closure = []
total = 0
for i in range(1682):
	print i
	result = trans_clos.trans_closure(i+1)
	all_closure.append(result)
	total += len(result)

total = float(total)/1682
print "avg_size:",total

with open("dumps/all_closure_list.pickle","wb") as dump:
	pickle.dump(all_closure,dump)
	
print "Time:",time.time() - start_time