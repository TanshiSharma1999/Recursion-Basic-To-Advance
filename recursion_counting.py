# Print numbers from 1 to n using recursion.
def show(n):
    if n<1:
        return
    show(n-1)
    print(n)
    
show(5)

#Print numbers from n to 1 using recursion.
def reverse_show(n):
    if n<1:
        return
    print(n)
    reverse_show(n-1)
reverse_show(5)    
