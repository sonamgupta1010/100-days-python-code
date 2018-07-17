vowel='aeiou'
ip_str='Hello,would you like to tea?'
ip_str=ip_str.casefold()
count={}.fromkeys(vowel,0)
for char in ip_str:
    if char in count:
        count[char]+=1
print (count)        
