arra1=["aaa","bbb","ccc","ddd","aaa","bbb","ccc","bbb","bbb","bbb","ccc"]
b = []
unique = []
k=0
for i in range(0,len(arra1)):

    presense=False
    for check in range(0,len(unique)):
        presense=False
        if(arra1[i]==unique[check]):
            presense=True
            break
        if(presense==True):break


    if(presense==False):
        unique.append(arra1[i])
        count=0
        b.append(arra1[i])


        for j in range(i,len(arra1)):

            if(arra1[i]==arra1[j]):
                count=count+1
        b.append(count)

#continue with highest number of occurence of words
print(b)
occur = []
occurword = []
for i in range(1,len(b),2):
    occur.append(b[i])

for i in range(0,len(b),2):
    occurword.append(b[i])

print(occur)
print(occurword)

seq=occur.copy()
seqword=occurword.copy()

for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            seqword[j - 1], seqword[j] = seqword[j], seqword[j - 1]
            j -= 1
seq.reverse()
seqword.reverse()
print(seq)
print(seqword)

#after merge
aftersort = []
for i in range(0,int((len(b))/2)):
    aftersort.append(seqword[i])
    aftersort.append(seq[i])
print(aftersort)



