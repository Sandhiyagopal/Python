class Sandhiya:
    def __init__(self,firstname,lastname,id):
        self.efirstname=firstname
        self.elastname=lastname
        self.id=id
    def getDetails(self):
        print(self.efirstname)

#Use pass keyword
class Gopal(Sandhiya):
    pass

s=Gopal("keethu","prabu",103)
s.getDetails()
print(s.elastname)
print(s.id)

    

