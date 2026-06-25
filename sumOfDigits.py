#logic
'''x=23451

x=str(x)

print(int(x[0])+int(x[1])+int(x[2])+int(x[3])+int(x[4]))
'''
#solution
def sums(n):
    n=str(n)
    if len(n)==1:
        return 1
    elif len(n)<1:
        return
    return int(n[0])+(sums(n[1:]))

x=sums(23451)
print(x)