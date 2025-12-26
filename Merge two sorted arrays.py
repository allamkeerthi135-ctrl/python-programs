s=[1,2,5,7]
s2=[3,6,8,10]
i=0
j=0
res=[]
while i<len(s) and j<len(s2):
    if s[i]<s2[j]:
        res.append(s[i])
        i+=1
    else:
        res.append(s2[j])
        j+=1
while i<len(s):
    res.append(s[i])
    i+=1
while j<len(s2):
    res.append(s2[j])
    j+=1
print(res)
