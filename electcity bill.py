u=int(input("enter unit consumped:"))
if u<=50:
    pa=u*0.20
elif u<=150:
    pa=(50*0.20)+(u-50)*0.50
elif u<=250:
    pa=(50*0.20)+(150-50)*0.50+(u-150)*1.20
elif u>250:
    pa=(50*0.20)+(150-50)*0.50+(u-150)*1.20+(u-250)*1.75
total=pa
print("total bill:",total)
