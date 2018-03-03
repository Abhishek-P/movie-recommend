import pickle

with open("dumps/user_vs_movie.pickle", "rb") as user_movie_matrix_dump:
    user_movie = pickle.load(user_movie_matrix_dump)
occ = open("source_data\u.occupation", "r")
occ = [i.strip("\n") for i in occ.readlines()]
uocc = open("source_data\u.user", "r")
uocc = uocc.readlines()
for i in range(len(uocc)):
    uocc[i] = uocc[i].split("|")[3]
# occupation matrix
occ_matrix = []

for i in range(1682):
    temp = dict()
    for h in occ:
        temp[h] = 0
    occ_matrix.append(temp)

# print len(user_movie),len(uocc),len(occ_matrix)

for i in range(len(user_movie)):
    for j in range(len(user_movie[i])):
        if user_movie[i][j] != 0:
            occ_matrix[j][uocc[i]] += 1
        else:
            pass
occ_movie_dump = open("dumps/occupation_movie.pickle", "wb")
pickle.dump(occ_matrix, occ_movie_dump)
occ_movie_dump.close()
