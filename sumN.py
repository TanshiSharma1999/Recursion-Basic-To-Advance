#WAP to write Sum of n natural numbers using recursion

def Sum(num):
    if num <=0:
        print("Not a natural number.")
    elif num==1:
        return 1        
    return num+Sum(num-1)
n=int(input("Enter number: "))
x=Sum(n)
print(x)    