""" Extraction of data for each item in the dataset
The format is as follows

u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.
	      
It is to be converted into a dictionary with movie id as key and a dict containing the details as value
movie title - string
release date - string
video release date string
imdb URL
Genre: Set of strings
The delimiter here is "|" on which split will be performed
The release dates although available, are not used for any purposes at this time.
The read is done at once"""
import time
import pickle

start_time = time.time()
items = dict()  # the items dict
lines = None  # to contain the read data line by line

genre_dict = {5: "Unknown", 6: "Action", 7: "Adventure", 8: "Animation",
              9: "Children's", 10: "Comedy", 11: "Crime",
              12: "Documentary", 13: "Drama", 14: "Fantasy",
              15: "Film-Noir", 16: "Horror", 17: "Musical", 18: "Mystery", 19: "Romance", 20: "Sci-Fi",
              21: "Thriller", 22: "War", 23: "Western"}
with open("source_data\u.item", "r") as items_input:
    lines = items_input.readlines()

for i in lines:
    line = i.split("|")
    id = int(line[0])
    items[id] = dict()
    items[id]["name"] = line[1]
    items[id]["release_date"] = line[2]
    items[id]["v_release_date"] = line[3]
    items[id]["url"] = line[4]
    items[id]["genre"] = set()
    for j in xrange(5, 24):
        if line[j] == "1":
            items[id]["genre"].add(genre_dict[j])

with open("dumps/items.pickle", "wb") as items_dump:
    pickle.dump(items, items_dump)

print len(items)
print "Time:", time.time() - start_time
