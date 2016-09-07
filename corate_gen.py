"""
The co-rating count is the analagous of co-visitation counts in youtube
The co-rating matrix will be 1682 vs 1682 symmetric matrix
where i,j will be the no. of users who have watched both
The user_movies_dump or the user_vs_movies_dump can be used to generate the same
It will then be dumped int movie_corate_matrix
Here user_movies is used.
Since python is 0-indexed, -1 should be used while indexing
Brute-force
@author : Abhishek P, Bharath Kashyapa, Akshay A Malpani """
import pickle
import time
start_time = time.time()

movie_corate_matrix = [[0 for x in range(1682)] for y in range(1682)]

user_movies = pickle.load(open("dumps/user_movies.pickle","rb"))
for i in user_movies:
	temp = user_movies[i]
	for j in range(len(temp)):
		for k in range(j+1,len(temp)):
			movie_corate_matrix[temp[j]-1][temp[k]-1] = movie_corate_matrix[temp[j]-1][temp[k]-1] + 1
			movie_corate_matrix[temp[k]-1][temp[j]-1] = movie_corate_matrix[temp[j]-1][temp[k]-1]
for i in range(10):
	print movie_corate_matrix[i][:10]
			
		
movie_corate_matrix_dump = open("dumps/movie_corate_matrix.pickle","wb")
pickle.dump(movie_corate_matrix,movie_corate_matrix_dump)
# movie_corate_matrix_dump.close()


		
print "Time:",time.time() - start_time
