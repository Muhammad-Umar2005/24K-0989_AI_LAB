def Salary(basicsalary):
    hra=0.1*basicsalary
    da=(5/100)*basicsalary
    totalsalary=basicsalary+hra+da
    return totalsalary

print("Total Salary is:",Salary(int(input("Enter Basic Salary: "))))