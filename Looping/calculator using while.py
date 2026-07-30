while True:
    print("1.addition")
    print("2.substration")
    print("3.multiplication")
    print("4.division")
    choice=int(input())
    if choice==5:
        print("thank you")
        break
    a=int(input())
    b=int(input())
    if choice==1:
        print("add=",a+b)
    elif choice==2:
        print("sub=",a-b)
    elif choice==3:
        print("mul=",a*b)
    elif choice==4:
        print("div=",a/b)
    else:
        print("invalid")
        
