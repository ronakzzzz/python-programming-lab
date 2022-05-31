st=str(input("enter a name:"))
flag=0
for i in range(0,len(st)):
    if flag==0:
        print(st[i].lower())
        flag=1
    elif flag==1:
        print(st[i].upper())
        flag=0
