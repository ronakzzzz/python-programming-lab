s=0
a=input("Enter the list").split()
num_lst=list(map(int,a))
for i in num_lst:
    if i%2==0:
        s=s+i
print(s)
