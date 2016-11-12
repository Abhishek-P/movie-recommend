import pickle
import time

def trans_closure(uid):
	with open("dumps/symmetric_movie_matrix.pickle","rb") as norm_movie_matrix:
			norm_matrix=pickle.load(norm_movie_matrix)
	with open("dumps/baselist_40.pickle","rb") as norm_movie_matrix:
			baselistoflists=pickle.load(norm_movie_matrix)
	
	
	lvl1_complete=[]
	baselist=baselistoflists[uid]  # all movies watched by user and their respective ratings [(movie,rating)...]
	
	for ind_movie_index in range(len(baselist)):
	    watched_movie=baselist[ind_movie_index][0]
	    list_score_of_related_movies_of_watched=norm_matrix[watched_movie]
	    to_sort=[]
	    for i in range(len(list_score_of_related_movies_of_watched)):
	        to_sort.append((i,list_score_of_related_movies_of_watched[i]))
	    x=sorted(to_sort,key=lambda student: student[1],reverse=True) # 
	    temp_lvl1=x[:20]
	    #Tuple format (base_movie,related_movie,edge_weight,lvl)
	    for x in temp_lvl1:
	        lvl1_complete.append([watched_movie,x[0],x[1],1])
	for i in range(len(lvl1_complete)):
	    for j in range(i+1,len(lvl1_complete)):
	        if lvl1_complete[i][1]==lvl1_complete[j][1]:
	            lvl1_complete[j][2]=float(format((lvl1_complete[j][2]+lvl1_complete[i][2])*0.2, '.2f'))
	            lvl1_complete[i][3]=-1
	#print len(lvl1_complete),"\n"
	lvl1_final=[]
	for i in range(len(lvl1_complete)):
	    if lvl1_complete[i][3]>0:
	        lvl1_final.append(lvl1_complete[i])
	#print len(lvl1_final)
	lvl1=sorted(lvl1_final,key=lambda x:x[2],reverse=True)
	#print lvl1
	
	lvl2_complete=[]
	for ind_movie_index in range(len(lvl1)):
	    watched_movie=lvl1[ind_movie_index][1]
	    list_score_of_related_movies_of_watched=norm_matrix[watched_movie]
	    to_sort=[]
	    for i in range(len(list_score_of_related_movies_of_watched)):
	        to_sort.append((i,list_score_of_related_movies_of_watched[i]))
	    x=sorted(to_sort,key=lambda student: student[1],reverse=True) # 
	    temp_lvl2=x[:8]
	    for x in temp_lvl2:
	        lvl2_complete.append([lvl1[ind_movie_index][0],x[0],(lvl1[ind_movie_index][2]*0.25+x[1]),2])
	for i in range(len(lvl2_complete)):
	    for j in range(i+1,len(lvl2_complete)):
	        if lvl2_complete[i][1]==lvl2_complete[j][1] or lvl2_complete[i][0]==lvl2_complete[i][1]:
	            lvl2_complete[j][2]=float(format((lvl2_complete[j][2]+lvl2_complete[i][2])*0.25, '.2f'))
	            lvl2_complete[i][3]=-1
	#print len(lvl1_complete),"\n"
	lvl2_final=[]
	for i in range(len(lvl2_complete)):
	    if lvl2_complete[i][3]>0:
	        lvl2_final.append(lvl2_complete[i])
	#print len(lvl1_final)
	lvl2=sorted(lvl2_final,key=lambda x:x[2],reverse=True)
	final_list_lvl1=[]
	final_list_lvl2=[]
	final_length=0
	for i in range(len(lvl1_final)):
	    count=0
	    for x in final_list_lvl1:
	        if lvl1_final[i][0]==x :
	            count+=1
	    if count<=2:
	        final_list_lvl1.append(lvl1_final[i][1])
	        final_length+=1
	    #if final_length>10:
	    #    break
	final_length=0
	for i in lvl2:
	    if i[1] in final_list_lvl1:
	        pass
	    else:
	        final_list_lvl2.append(i[1])
	        final_length+=1
	    #if final_length>5:
	    #    break
	#print len(final_list_lvl1), len(final_list_lvl2)
	#print final_list_lvl1,final_list_lvl2
	return final_list_lvl1 + final_list_lvl2
	
if __name__ == "__main__":
	start_time = time.time()
	
	result  = trans_closure(2)
	print len(result)
	
	print "time:",time.time() -  start_time