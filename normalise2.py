import pickle
import time
start_time = time.time()
with open("dumps/user_vs_movie.pickle","rb") as user_movie_matrix_dump:
		user_movie=pickle.load(user_movie_matrix_dump)
print len(user_movie)
no_of_reviews=[0]*1682
for i in range(len(user_movie)):
    for j in range(len(user_movie[i])):
        if user_movie[i][j]>0:
            no_of_reviews[j]+=1
print max(no_of_reviews),min(no_of_reviews)
