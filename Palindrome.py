s = "madam"
res = ""
for i in range(-1, -len(s)-1, -1):
    res = res + s[i]

if s == res:
    print("palindrome")
else:
    print("not a palindrome")
