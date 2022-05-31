salary=int(input("enter the salary:"))
if salary<10000:
    salary=salary+(0.75*salary)+(0.70*salary)
    print("total salary is:",salary)
elif salary>10000 and salary<20000:
    salary=salary+(0.80*salary)+(0.80*salary)
    print("total salary is :",salary)
elif salary>20000:
    salary=salary+(0.90*salary)+(0.95*salary)
    print("total salary is:",salary)
