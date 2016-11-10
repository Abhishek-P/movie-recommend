import pickle
with open("dumps/user_vs_movie.pickle","rb") as user_movie_matrix_dump:
		user_movie=pickle.load(user_movie_matrix_dump)
user_details=open("u.item","r")
movie_names=[i.strip("\n") for i in user_details.readlines()]
user_movie_name=[]
for i in range(len(movie_names)):
	movie_names[i]=movie_names[i].split("|")[1]
#print movie_names
for i in range(len(user_movie)):
	temp=[]
	for j in range(len(user_movie[i])):
		if user_movie[i][j]!=0:
			temp.append(movie_names[j])	
		else:	
			pass
	user_movie_name.append(temp)
norm_movie_dump = open("dumps/movie_names_for_user","wb")
pickle.dump(user_movie_name,norm_movie_dump)
norm_movie_dump.close()

