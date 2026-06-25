'''
*****
****
***
**
*

'''
def pattern(n):
    if n<0:
        return
    elif n==1:
        return "*"
    return("*"*n+"\n")+pattern(n-1)

x=pattern(5)
print(x)
'''
*
**
***
****
*****
'''
print("\n \n")
def pattern(n):
    if n<0:
        return
    elif n==1:
        return "*"
    return pattern(n-1)+"\n"+("*"*n)

x=pattern(5)
print(x)