#Count the number of digits in a number.
def count_digits(n):
    n = abs(n)   # handles negative numbers

    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(121234534))    