import pickle
import time
start_time = time.time()
with open("dumps/movie_corate_matrix.pickle","rb") as movie_corate_matrix_dump:
	movie_corate_matrix = pickle.load(movie_corate_matrix_dump)
corate_count = open("logs/avg_corate_count.txt","w")

avg_count = 0
for i in range(len(movie_corate_matrix)):
	for j in range(len(movie_corate_matrix)):
		if( not i == j):
			avg_count = avg_count + movie_corate_matrix[i][j]
avg_count = (avg_count/2)
avg_count = avg_count/len(movie_corate_matrix)
corate_count.write("Average co-rating count:"+str(avg_count)+"\n")
corate_count.write("Time: "+str(time.time()-start_time)+"\n")
corate_count.close()