start=int(input())
end=int(input())
for i in range(start,end):
    if(i%400==0)or(i%4==0 and i%100!=0):
        print(i)
        
        
