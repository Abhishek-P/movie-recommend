import pickle
import time
start_time = time.time()

def ranking(user_id, candidate_set):
	avg_age = pickle.load(open("dumps/avg_age.pickle","rb"))
	no_of_females = pickle.load(open("dumps/no_of_females.pickle","rb")
	no_of_males = pickle.load(open("dumps/no_of_males.pickle","rb"))
	occupation_matrix = pickle.load(open("dumps/occupation_matrix.pickle","rb"))
	given_user_vs_movies  = pickle.load(open("dumps/user_vs_movie","rb"))[movie_id - 1]
	