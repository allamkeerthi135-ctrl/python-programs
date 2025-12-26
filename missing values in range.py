s=[1,2,4,5,6,7,8,9]
missing=[]
for i in range(min(s),max(s)+1):
    if i not in s:
        missing.append(i)
print(missing)
