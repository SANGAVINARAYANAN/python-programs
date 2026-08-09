n=int(input())
data={}
for i in range(n):
    k=int(input())
    v=input()
    data[k]=v
print(data)
print("keys:",data.keys())
print("values:",data.values())
print("items:",data.items())
