class Emplo:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print_emp(self):
        print(self.ename)
f=open("filemap")
employees=[]
for lines in f:
    eid,ename,desig,salary=lines.rstrip("\n").split(",")
    e1=Emplo(eid,ename,desig,salary)
    employees.append(e1)
# b2=Emplo(101,"manu","R&D",25000)
# b3=Emplo(102,"maya","manager",21000)
# b4=Emplo(103,"jittu","sw tester",28000)
# employee=[]
# employee.append(b1)
# employee.append(b2)
# employee.append(b3)
# employee.append(b4)

# sal=[]   CONVENTIONAL APPROACH
# for emp in employee:
#     sal.append(emp.salary)
# print(sal)
salary=list(map(lambda emp:emp.salary,employees))
hs=max(salary)
print(salary)
print(hs)
developer=list(filter(lambda emp:emp.desig=='developer',employees))
print(developer)