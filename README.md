# movie-recommend
## Guide: Prof. Srinivas Murthy
###Developers: Abhishek P, Akshay A Malpani, Bharath Kashyapa

Youtube Style Movie Recommendation:
An effort to adapt the youtube recommendation for a movie dataset

###Legend:

corate_gen - generates corate matrix from user_movies
extract - record to user_vs_movie and user_movies
dict2list - converts a pickled dict to list with keys as index
avg_corate_count.py - generates average corate count from 'movie_corate_matrix.pickle'

dumps/
user_movies.pickle -  pickle of user vs movie list dict over 100k
user_vs_movie.pickle - pickle of user vs movie rating matrix 
records.pickle - the 100k records stores as a list of list
movie_corate_matrix.pickle - pickle of corating symmetric matrix of movies
 
logs/
avg_corate_count.txt - result og avg_corate_count.py - contains average corate count per movie