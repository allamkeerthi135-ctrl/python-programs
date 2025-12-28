def combination(n,k,curr,start):
    if len(curr)==k:
        print(curr)
        return
    for j in range(start,n+1):
        curr.append(j)
        combination(n,k,curr,start+1)
        curr.pop()
combination(4,2,[],1)