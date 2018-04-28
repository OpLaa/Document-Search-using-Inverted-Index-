'''n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])

# Output: 5
print(n_list[1][3])
'''
import glob
import os

#if(False):
a=[]
x="i am an idiot fellow-how are you"
a=x.split('-')
print(a)

cwd = os.getcwd()# Get the current working directory (cwd)
cwd=cwd+'/dataset'
print("CURRENT WORKING DIRRECTORY"+cwd)




files = []

print("CURRENT WORKING DIRECTORY\n\n" + str(cwd))
for i in os.listdir(cwd):
    if i.endswith('.txt'):
        files.append(i)
print("\n\n" + str(files))

final = []
a=[]
b=[]
a=["aaa","bbb","ccc"]
b=["ddd","eee","fff"]
print(a)
i=0
final.insert(i,a)
final.insert(1,b)
print(final)

qurres = []
a=['c',3,[23,45,56],'b',1,[6]]
query="b"
for i in range(0,len(a),3):
    if a[i] == query:
        qurres.append(a[i])
        qurres.append(a[i+1])
        qurres.append(a[i+2])
print(qurres)


list1 = ['1', '2', '3']
str1 = ','.join(list1)
print(str1)



query="College shivamogga"
word="i"
resultindex=['College', 'document1', 3, [13, 14, 15], 'document2', 3, [31, 39, 55], 'document3', 1, [1], 'shivamogga', 'document1', 3, [16, 17, 25], 'document2', 3, [22, 32, 44], 'i', 'document1', 2, [3, 18], 'am', 'document1', 2, [4, 19]]
querylist=query.split()

indexword=[]

index=resultindex.index(word)+1
indexword.append(word)
for i in range(index,len(resultindex)):
    if resultindex[i] in querylist:
        break
    else:
        indexword.append(resultindex[i])

print(indexword)
print(index)
print('after printing')




#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in '%s': %s" % (cwd, files))


