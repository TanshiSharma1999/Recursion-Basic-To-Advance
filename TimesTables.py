#times table with recursion

def multipleTable(n,i=1):
    if i>10:
        return
    print(f"{n}x{i}={n*i}")
    multipleTable(n,i+1)

multipleTable(12)    
