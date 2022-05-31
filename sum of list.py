out=input("enter the list").split()
num_lst=[]
for i in out:
    num_lst.append(int(i))
s=sum(num_lst)
print("sum",s)
