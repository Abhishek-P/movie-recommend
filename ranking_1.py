import pickle
import time
import trans_clos
start_time = time.time()
score = dict()
def ranking(user_id):
	avg_age = pickle.load(open("dumps/avg_age.pickle","rb"))
	avg_rating = pickle.load(open("dumps/avg_rating.pickle","rb"))
	items = pickle.load(open("dumps/items.pickle","rb"))
	occupation_movie = pickle.load(open("dumps/occupation_movie.pickle","rb"))
	#given_user_vs_movies  = pickle.load(open("dumps/user_vs_movie","rb"))[movie_id - 1]
	user_details = pickle.load(open("dumps/user.pickle","rb"))
	
	candidate_set = trans_clos.trans_closure(2)
	
	for i in range(len(candidate_set)):
		candidate_set[i] += 1
		
	for i in candidate_set:
		score[i] = 0
		#print (avg_age[i-1] - user_details[user_id]["age"])
		#print float(occupation_movie[i-1][user_details[user_id]["occupation"]])/(items[i]["males"] + items[i]["females"])
		if user_details[user_id]["gender"] == "M":
			val = items[i]["males"]
		else:
			val = items[i]["females"]
		#print float(val)/(items[i]["males"] + items[i]["females"])
		#print avg_rating[i - 1]/5
		score[i] += float(occupation_movie[i-1][user_details[user_id]["occupation"]])/(items[i]["males"] + items[i]["females"])
		score[i] += avg_rating[i - 1]/5
		score[i] += float(val)/(items[i]["males"] + items[i]["females"])
		score[i] += float(1)/abs(avg_age[i-1] - user_details[user_id]["age"])
		#print score[i]
		
	ranked_list = []
	
	for i in score:
	#	print i,score[i]
		ranked_list.append((i,score[i]))
	ranked_list = sorted(ranked_list, key = lambda x:x[1], reverse = True)
	
	#for i in ranked_list:
	#	print i
	return (candidate_set,ranked_list[:20])
if __name__ == "__main__":
	for i in ranking(2):
		print i
	print "Time:",time.time() - start_time