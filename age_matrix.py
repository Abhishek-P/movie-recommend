import pickle
with open("dumps/user_vs_movie.pickle","rb") as user_movie_matrix_dump:
		user_movie=pickle.load(user_movie_matrix_dump)
uage=open("u.user","r")
uage=uage.readlines()
for i in range(len(uage)):
	uage[i]=int(uage[i].split("|")[1])
age_aggr=[0]*1682
no_viewers=[0]*1682
for i in range(len(user_movie)):
	for j in range(len(user_movie[i])):
		if user_movie[i][j]!=0:
			age_aggr[j]+=uage[i]
			no_viewers[j]+=1
		else:	
			pass
for i in range(len(age_aggr)):
	age_aggr[i]=age_aggr[i]/float(no_viewers[i])
	age_aggr[i]=float(format(age_aggr[i], '.2f'))

norm_movie_dump = open("dumps/avg_age.pickle","wb")
pickle.dump(age_aggr,norm_movie_dump)
norm_movie_dump.close()
