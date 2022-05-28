a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b:
    if a>c:
        print("greatest no. is a:",a)
    else:
        print("greatest no. is c:",c)
elif b>c:
    if b>a:
        print("greatest no. is b:",b)
    else:
        print("greatest no. is c:",c)
else:
    print("greatest no. is c:",c)
