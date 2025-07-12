n=int(input())
d=list(map(int, input().split()))
k=list(map(int, input().split()))
l=int(input())
d.sort()
k.sort(reverse=True)


t=0
for i in range(n):
    s=d[i] + k[i]
    if s > l:
        t+=(s-l)
print(t*100)

    