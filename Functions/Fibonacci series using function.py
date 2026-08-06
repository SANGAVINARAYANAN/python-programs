def fibonacci_series(n):
    series=[]
    a,b=0,1
    for i in range(n):
        series.append(a)
        a,b=b,a+b
    return series
n=int(input())
print(fibonacci_series(n))
