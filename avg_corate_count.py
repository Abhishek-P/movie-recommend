import pickle
import time
start_time = time.time()
with open("dumps/movie_corate_matrix.pickle","rb") as movie_corate_matrix_dump:
	movie_corate_matrix = pickle.load(movie_corate_matrix_dump)
corate_count = open("logs/avg_corate_count.txt","w")

avg_count = 0
min = 1000
max = 0
for i in range(1682):
	for j in range(i+1,1682):
			if( movie_corate_matrix[i][j] < min ):
				min = movie_corate_matrix[i][j]
			elif( movie_corate_matrix[i][j] > max ):
				max = movie_corate_matrix[i][j]
			avg_count = avg_count + movie_corate_matrix[i][j]
avg_count = avg_count/(1682*840)
corate_count.write("Max is "+str(max)+" and min is "+str(min)+"\n")
corate_count.write("Average co-rating count is "+str(avg_count)+"\n")
corate_count.write("Time: "+str(time.time()-start_time)+"\n")
corate_count.close()