s="keerthi"
res=""
for char in s:
    if 'a'<= char<='z':
        res+=chr(ord(char)-32)
    else:
        res+=char
print(res)
