def reversestring(s):
    
    if len(s) == 1:
        return s[0]
    
    firstchar = s[0]

    return reversestring(s[1:]) + firstchar

s=input("Enter a word:")
print(reversestring(s))