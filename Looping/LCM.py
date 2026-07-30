a=int(input())
b=int(input())
x,y=a,b
while b!=0:
    a,b=b,a%b
    lcm=(x*y)//a
print(a)
