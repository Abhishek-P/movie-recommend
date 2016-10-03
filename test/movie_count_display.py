"""
@author : Abhishek P, Bharath Kashyapa, Akshay A Malpani
/test/movie_count_display.py
to get an idea about the counts, although average is 100k/1682"""
import pickle
import time 
start_time = time.time()
with open("../dumps/movie_count.pickle") as movie_count_dump:
    movie_count = pickle.load(movie_count_dump)

min = 1000
mean = 100000/1682
variance = 0
max = 0
for i in range(len(movie_count)):
    if( movie_count[i] > max ):
        max = movie_count[i]
		
        
    if(movie_count[i] < min ):
        min = movie_count[i]
        
    variance = variance + ((movie_count[i] - mean)**2)*(movie_count[i]/float(100000))
    print i+1 , movie_count[i]
variance = variance**0.5

print min,max, ". mean:", mean, ". variance:", variance
print "Time:",time.time() - start_time