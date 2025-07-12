n=int(input())
k=[input().split() for _ in range(n)]
# for j in range(n):
#     k=[input().strip()]
stack=[]
i=0
while i<n:
    
    l=k[i]
    r=l[0]
    if r=="PUSH":
        #stack=k[i+1]
        stack.append(int(l[1]))

    elif r=="STORE":
        register=stack.pop()
    elif r=="LOAD":
        stack.append(register)


    elif r== "PLUS":
        g=stack.pop()
        h=stack.pop()
        d=g+h
        stack.append(d)

    elif r=="TIMES":
        g=stack.pop()
        h=stack.pop()
        d=g*h
        stack.append(d)
   
    elif r=="IFZERO":
        v=stack.pop()
        if v==0:
            i=int(l[1]) - 1  
    elif r=="DONE":
        print(stack.pop())
        break
    i=i+1
        