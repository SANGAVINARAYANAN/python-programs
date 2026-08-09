n=int(input())
dict={}
for i in range(n):
    k=int(input())
    v=input()
    dict[k]=v
print(dict)
x=int(input("enter the num:"))
y=input("enter the value:" )
dict[x]=y
dict.update(dict)
print(dict)
dict.pop(1)
print(dict)

    
          
