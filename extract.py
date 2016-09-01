"""
The data, in form of 100k records has to be extracted and formed into a user vs movie rating matrix	and user vs watched movie list

The initial record 
user id, movie id, rating, timestamp
are read and stored in a list of lists - records
The first one is a matrix so its a list of lists
user vs watched movies on the other hand can be a dictionary of lists
We need a persisitent way to store these values since the size is vast
Current choices are RDBMS and Pickle dump
@author : Abhishek P, Bharath Kashyapa, Akshay A Malpani """
import time
import pickle
start_time = time.time()
file = open("u.data","r")
records = []
for i in range(100000):
	records.append(file.readline().rstrip().split("\t"));
file2 = open("records.pickle","wb")
pickle.dump(records,file2);
file2.close()

# converting the strings to int, float
for i in records:
	i[0] = int(i[0])
	i[1] = int(i[1])
	i[2] = float(i[2])

#generate the user vs movies list okay
user_movies = {}
for i in records:
	if( i[0] not in user_movies):
		user_movies[i[0]] = list()
	user_movies[i[0]].append(i[1])
user_movies_dump = open("user_movies.pickle","wb")
pickle.dump(user_movies,user_movies_dump)
user_movies_dump.close()

#lets generate the user vs movie matrix with 0 or ratings at user id, movie id
user_vs_movie = [[0 for x in range(943)] for y in range(1682)]
for i in records[:10]:
	user_vs_movie[i[0]][i[1]] = i[2]

user_vs_movie_dump = open("user_vs_movie.pickle","wb")
pickle.dump(user_vs_movie,user_vs_movie_dump)
user_vs_movie_dump.close()
print "Time:",time.time() - start_time

