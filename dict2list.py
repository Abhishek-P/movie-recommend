"""
@lang = python 2.7
@author = Abhishek P
program converts pickled dict to pickle list ( only if keys are integers)
the name are given as command line arguments """
import sys
import pickle
import time
start_time = time.time()

def dict_to_list( d ):
	l = [ list() for x in range(len(d))]
	for i in d:
		l[i-1]  = d[i]
	return l
	
if __name__ == "__main__":
	list_dump = open(sys.argv[2], "wb")
	with  open(sys.argv[1], "rb")	 as dict_dump:
		pickle.dump(dict_to_list(pickle.load(dict_dump)),list_dump)
	list_dump.close()
	