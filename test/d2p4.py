n,d = map(int,input().split())
s = 0
k=list(map(int,input().split()))
k.sort(reverse=True) 
for i in range(d):
    s=sum(k[:d])
print(s)
