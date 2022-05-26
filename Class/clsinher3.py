class Student:
    def __init__(self,sname,sid,sdept):
        self.name=sname
        self.id=sid
        self.dept=sdept
    def getStudent(self):
        print(self.name, self.id)
    def getStudentDetails(self):
        print(self.name,self.id,self.dept,self.year)
        
class Student1(Student):
    def __init__(self,sname,sid,sdept,spassedoutyear):
        super().__init__(sname,sid,sdept)
        self.year=spassedoutyear
    def getStudentDet(self):
        print(self.year)
    def getStudent2(self):
        print(self.name)
        
class Student3(Student1):
    pass
 
x=Student3("sandy",333,"CSE",2022)
x.getStudentDet()
x.getStudentDetails()
s=Student1("santhosh",303,"CSE",2020)
s.getStudentDetails()
s.getStudentDet()