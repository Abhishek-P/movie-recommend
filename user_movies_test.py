import pickle
import time
start_time = time.time()

user_vs_movie = pickle.load( open("dumps/user_vs_movie.pickle","rb"))
print type(user_vs_movie)
given_user_vs_movie = user_vs_movie[id-1]
