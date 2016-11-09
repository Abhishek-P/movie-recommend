import pickle
import time
start_time = time.time()
            
with open("dumps/user_vs_movie.pickle","rb") as user_movie_matrix_dump:
		user_movie=pickle.load(user_movie_matrix_dump)
print len(user_movie)

movie_movie=[[0]*1682 for _ in range(1682)]
for i in range(0,len(user_movie)):
    for j in range(0,len(user_movie[i])-1):
        k=j+1
        while k<=len(user_movie[i])-1:
            movie_movie[j][k]+=user_movie[i][j]*user_movie[i][k]
            k=k+1
movie_movie_dump = open("dumps/movie_movie.pickle","wb")
pickle.dump(movie_movie,movie_movie_dump)
movie_movie_dump.close()

'''
#print user_movie[0][0:10]
movie_movie=[[0]*10 for _ in range(10)]
#print movie_movie
for i in range(0,10):
    for j in range(0,9):
        k=j+1
        while k<=9:
            #if user_movie[i][j]>0 and user_movie[i][k]:
                #print i,j,k,user_movie[i][j],user_movie[i][k]
            movie_movie[j][k]=movie_movie[j][k]+(user_movie[i][j]*user_movie[i][k])
            k=k+1
for l in movie_movie:
     print l,"\n"
'''
print time.time()-start_time         
    
