import pickle
import time

with open("dumps/movie_movie.pickle","rb") as norm_movie_matrix:
		base=pickle.load(norm_movie_matrix)
		
print len(base),len(base[0])
for i in range(1682):
	for j in range(1682):
		if i>j:
			base[i][j]=base[j][i]
print base[0][:5],"\n\n",base[1][:5]
'''
uid=20  # when taking input minus 1

baselist=base[uid]

for i in range(len(baselist)):
	basemovie=baselist[i][0]
	lvl1=movie_norm[basemovie]            #
	for x in range(0,basemovie):
		lvl1[x]=movie_norm[x][basemovie]
	print lvl1
'''
norm_movie_dump = open("dumps/symmetric_movie_matrix.pickle","wb")
pickle.dump(base,norm_movie_dump)
norm_movie_dump.close()
