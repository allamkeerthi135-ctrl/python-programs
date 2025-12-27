s="sudying"
vowel_count=0
consonent_count=0
for char in s:
    if char in"aeiouAEIOU":
        vowel_count+=1
    else:
        consonent_count+=1
print("vowel",vowel_count)
print("consonent",consonent_count)
