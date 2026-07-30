n=int(input())
temp=n
total=0
for i in range(1,n):
    if n%i==0:
        total=total+i
if(total==temp):
    print("perfect number")
else:
    print("not perfect number")
