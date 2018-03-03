# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:41:36 2016

@author: Abhishek P Taula
"""

import pickle
import time

start_time = time.time()

input_file = open("source_data/u.user", "r")
user_details = dict()
input_text = input_file.readlines()
for i in range(943):
    user_details[i + 1] = dict()
    details = input_text[i].split("|")
    user_details[i + 1]["age"] = int(details[1])
    user_details[i + 1]["gender"] = details[2]
    user_details[i + 1]["occupation"] = details[3]

with open("dumps/user.pickle", "wb") as dump:
    pickle.dump(user_details, dump)

print "Time:", time.time() - start_time
