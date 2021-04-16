class Employee:
    def __init__(self,eid,ename,resig,salary):
        self.eid=eid
        self.ename=ename
        self.eresig=resig
        self.salary=salary
    def printval(self):
        print(self.ename)
    def __sizeof__(self):\
        return self.ename+self.resig
emp=Employee(1001,"anu","developer",25000)
emp1=Employee(1002,"manu","R&D",29000)
empl=[]
empl.append(emp)
empl.append(emp1)
dev=list(filter(lambda emp:emp.resig=='developer',empl))
for em in dev:
    print(em)
