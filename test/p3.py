s=input().strip()
stack=[]
for c in s:
    if c=="{":
        stack.append("{")    
    elif c=="}":
        if not stack:
            print("Not Matching")
            break
        stack.pop()
else:
    if not stack:
        print("Matching")
    else:
        print("Not Matching")