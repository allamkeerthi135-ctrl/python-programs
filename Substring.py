def substring(s,ans):
    if len(s)==0:
        print(ans)
        return
    substring(s[1:],ans +s[0])
    substring(s[1:],ans)
substring("abc","")
