dict1={}
n=int(input("enter first dictionary:"))
for i in range(n):
    k=int(input("number:"))
    v=input("values:")
    dict1[k]=v
dict2={}
n=int(input("enter second dictionary:"))
for i in range(n):
    k=int(input("number:"))
    v=input("values:")
    dict2[k]=v
dict1.update(dict2)
print("merged dictionary:",dict1)

