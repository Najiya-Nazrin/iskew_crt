n=int(input())
array=list(map(int,input().split()))
target=int(input())
# i=0
# j=1
found= False
for i in range(n):
    for j in range(i+1,n):
        s=array[i]+array[j]
        if s==target:
            found = True
            break
if not found:
    print("No")
else:
    print("Yes")