import pickle
import time

with open("dumps/norm_movie.pickle","rb") as norm_movie_matrix:
		movie_norm=pickle.load(norm_movie_matrix)
with open("dumps/user_vs_movie.pickle","rb") as user_movie_matrix:
		user_movie=pickle.load(user_movie_matrix)
baselist=[]

'''
avg_usr=[]
for i in range(len(user_movie)):
	count=0
	sum=0
	for j in range(len(user_movie[i])):
		if user_movie[i][j]!=0:
			count+=1
			sum+=user_movie[i][j]
		else:
			pass
	avg_usr.append(sum/float(count))

	'''
for i in range(len(user_movie)):
	tosort=[]
	for j in range(len(user_movie[i])):
		if user_movie[i][j]!=0:
			tosort.append((j,user_movie[i][j]))
	x = sorted(tosort,key=lambda student: student[1],reverse=True)
	baselist.append(x[:40])
for k in baselist:
        print k,"\n"
norm_movie_dump = open("dumps/baselist_40.pickle","wb")
pickle.dump(baselist,norm_movie_dump)
norm_movie_dump.close()

