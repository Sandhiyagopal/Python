class Employee:
    def __init__(self,name,id,mobile,salary):
        self.sname=name
        self.sid=id
        self.smobile=mobile
        self.esalary=salary
    def getEmployee(self):
        print(self.sname,self.sid)
    def getEmployeeDetails(self):
        print(self.sname,"\n",self.sid,"\n",self.smobile,"\n",self.esalary)

class Employee1(Employee):
    pass
class Employee2(Employee1):
    pass

E=Employee1("sandy",303,9876543210,40000)
E.getEmployee()
E.getEmployeeDetails()

E1=Employee2("sangee",305,9999988888,45000)
E1.getEmployeeDetails()


        