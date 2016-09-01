import time
start_time = time.time()
file=open("u.data","r")
k=[]
for i in range(100000):
    k.append(file.readline().strip().split("\t"))
#print(k)
'''m=[[0]*1682]*943    users vs movies
for i in range(len(k)):
    m[int(k[i][0])][int(k[i][1])]=1
for i in m:
    print(i)'''
m = {}                   #movies vs users
for i in k:
    if( i[1] not  in  m):
        m[i[1]] = []
    m[i[1]].append(i[0])
count=0
for i in m:
    if(len(m[i])>1):
        print(i,m[i])
        count = count + 1
print(count)
print( time.time() - start_time) 

