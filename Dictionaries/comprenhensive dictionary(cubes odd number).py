n=int(input())
oddcubes={x:x*x*x for x in range(1,n)if x%2!=0}
print(oddcubes)
print(type(oddcubes))
