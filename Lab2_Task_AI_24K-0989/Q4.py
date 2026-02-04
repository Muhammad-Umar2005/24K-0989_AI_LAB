class Employee:
    def work(self):
        print("Employee is working.")


class Manager(Employee):
    def work(self):
        print("Manager is planning and managing the team.")


class Developer(Employee):
    def work(self):
        print("Developer is writing and fixing code.")


class Designer(Employee):
    def work(self):
        print("Designer is creating designs and layouts.")


employees = [
    Manager(),
    Developer(),
    Designer()
]

for emp in employees:
    emp.work()
