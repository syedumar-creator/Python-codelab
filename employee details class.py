class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def show(self):
        print("Role:",self.role)
        print("Department:",self.dept)
        print("Salary:",self.salary)
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","EE",40000)
c1=engineer("Elon",33)
print(c1.name)
print(c1.age)
c1.show()