import pickle
with open("dumps/user_vs_movie.pickle","rb") as user_movie_matrix_dump:
		user_movie=pickle.load(user_movie_matrix_dump)

ug=open("u.user","r")
ug=ug.readlines()
for i in range(len(ug)):
	ug[i]=ug[i].split("|")[2]
no_of_F=[0]*1682
no_of_M=[0]*1682
for i in range(len(user_movie)):
	tempug=ug[i]
	for j in range(len(user_movie[i])):
		if user_movie[i][j]!=0:
			if tempug=='M':
				no_of_M[j]+=1
			else:
				no_of_F[j]+=1
		else:	
			pass
norm_movie_dump = open("dumps/no_of_females.pickle","wb")
pickle.dump(no_of_F,norm_movie_dump)
norm_movie_dump.close()

norm_movie_dump = open("dumps/no_of_males.pickle","wb")
pickle.dump(no_of_M,norm_movie_dump)
norm_movie_dump.close()
