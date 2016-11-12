import pickle
age_aggr = pickle.load(open("dumps/avg_age.pickle","rb"))
for i in age_aggr:
	print i,type(i)