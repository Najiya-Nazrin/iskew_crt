def factorial_number(n):
    if n == 1:
        return 1
    else:
        factorial=n * factorial_number(n-1)
        return factorial
n=int(input())
f=factorial_number(n)
print(f)
    