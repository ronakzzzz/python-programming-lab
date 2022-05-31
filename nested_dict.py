d={}
x=int(input("enter no. of elements:"))
for i in range(x):
    y=input()
    d[y]={}
    k=int(input())
    v=int(input())
    d[y].update({k:v})
print(d)
