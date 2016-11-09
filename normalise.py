import pickle
import time
start_time = time.time()
            
with open("dumps/movie_movie.pickle","rb") as movie_movie_matrix_dump:
		movie_movie=pickle.load(movie_movie_matrix_dump)
with open("dumps/movie_corate_matrix.pickle","rb") as movie_corate_matrix_dump:
	movie_corate_matrix = pickle.load(movie_corate_matrix_dump)
#print len(movie_movie),len(movie_corate_matrix)
#print len(movie_movie[-1]),len(movie_corate_matrix[-1])
norm_mm=[[0]*1682 for _ in range(1682)]
for i in range(len(norm_mm)):
               for j in range(i+1,len(norm_mm)):
                   if movie_corate_matrix!=0 and movie_corate_matrix[i][j]!=0:
                       norm_mm[i][j]=movie_movie[i][j]/float(movie_corate_matrix[i][j])
                       norm_mm[i][j]=format(norm_mm[i][j], '.4f')
norm_movie_dump = open("dumps/norm_movie.pickle","wb")
pickle.dump(norm_mm,norm_movie_dump)
norm_movie_dump.close()

