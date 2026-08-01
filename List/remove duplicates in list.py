n=list(map(int,input().split()))
t=[]
for i in n:
    if i not in t:
        t.append(i)
print(t)
