n=int(input("enter a no."))
y=n
r=0
while n!=0:
    d=n%10
    r=r*10+d
    n//=10
if y==r:
    print("p")
else:
    print("np")
