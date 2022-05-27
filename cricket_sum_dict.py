n = int(input("enter a n value:"))
d = {}
out=0
for i in range(n):
    keys = input() 
    values = int(input()) 
    d[keys] = values
    out=sum(d.values())
print(d)
print(out)
