from collections import Counter
n=int(input())
element=list(map(int,input().split()))
for i in range(n):
    c=Counter(element)
    if c[i] > 1:
        print("true")
        break

else:
    print("false")
