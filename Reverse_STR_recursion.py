#Reverse a string using recursion.
def REvStr(s):
    if s=="":
        return ""

    return REvStr(s[1:])+s[0]
    
s=input("Enter a string: ")
r=REvStr(s)
print(r)