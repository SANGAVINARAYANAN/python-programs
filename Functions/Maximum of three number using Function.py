def find_max(a,b,c):
    if(a>b and a>c):
        return "a is greater"
    elif(b>a and b>c):
        return "b is greater"
    else:
        return "c is greater"
a=int(input())
b=int(input())
c=int(input())
print(find_max(a,b,c))
