NumList=[]
Even_Sum=0
Odd_Sum=0
Number=int(input("Please enter the Total Number of List Elemente: "))
for i in range (1, Number + 1):
    value=int(input("enter the value od %d element:"%i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j]%2==0):
        Even_Sum=Even_Sum+NumList[j]
    else:
        Odd_Sum=Odd_Sum+NumList[j]

print("sum of even indexes:",Even_Sum)
print("sum of odd indexes:",Odd_Sum)
