list=list(map(int,input().split()))
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even=",even)
print("odd=",odd)
