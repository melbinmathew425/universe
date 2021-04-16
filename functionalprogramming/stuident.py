class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
obj1=Student(1001,"abc","c1",200)
obj2=Student(1002,"abm","c2",400)
obj3=Student(1003,"abg","c3",900)
stdlist=[]
stdlist.append(obj1)
stdlist.append(obj2)
stdlist.append(obj3)
sttotal=list(map(lambda std:std.total,stdlist))
print(sttotal)
print(max(sttotal))
