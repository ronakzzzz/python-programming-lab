n=int(input("enter a no."))
y=n**2
s=0
while y>0:
    d=y%10
    s=s+d
    y=y//10
if (n==s):
    print("neon")
else:
    print("not neon")
