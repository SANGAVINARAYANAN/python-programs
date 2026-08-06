def fact_value(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
a=int(input())
print(fact_value(a))
