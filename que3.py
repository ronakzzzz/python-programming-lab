s=input("enter b string")
t = ''
n=0
for i in range (len(s)):
    if ord(s[i])>=97 and ord (s[i])<=122:
        t +=chr(ord(s [i])-32)
    else:
        t+=chr (ord(s[i]))
for i in range (len(t)):
    if ord(t[0])==ord(t[i]):
        n=n+1
if n==len(t):
    print("all inputs are the same")
else:
    print("all inputs are not same")
