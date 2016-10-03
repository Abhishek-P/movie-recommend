import pickle
import time
start_time = time.time()

with open("dumps/movie_corate_matrix.pickle","rb") as movie_corate_matrix_dump:	
	movie_corate_matrix = pickle.load(movie_corate_matrix_dump)

with open("dumps/movie_count.pickle","rb") as movie_count_dump:
	movie_count = pickle.load(movie_count_dump)
	
normalized_corate_matrix = [[0 for x in xrange(1682)] for y in xrange(1682) ]
#print len(normalized_corate_matrix)
#print len(normalized_corate_matrix[0])

min_val = 1000
max_val = 0
sum = 0
variance = 0
for i in xrange(1682):
	for j in xrange(i+1,1682):
		normalized_corate_matrix[i][j] = float(movie_corate_matrix[min(i,j)][max(i,j)]) / (movie_count[i] * movie_count[j])
		
		sum += normalized_corate_matrix[i][j]
	
		if normalized_corate_matrix[i][j] < min_val :
			min_val = normalized_corate_matrix[i][j]
		
		if normalized_corate_matrix[i][j] > max_val :
			max_val = normalized_corate_matrix[i][j]

mean = sum/(1682 * 840)
for i in xrange(1682):
	for j in xrange(i+1,1682):
		variance = variance + ((normalized_corate_matrix[i][j] - mean)**2)*(normalized_corate_matrix[i][j]/sum)



with open("dumps/normalized_corate_matrix1.pickle","wb") as normalized_dump:
	pickle.dump(normalized_corate_matrix, normalized_dump)
	
print "min:",min_val
print "max:",max_val
print "mean:",mean
print "variance:",variance
print "Time:", time.time() - start_time