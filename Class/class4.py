class Classname:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print("This is constructor methods")
    def getClassname(self):
        print("GM")

C1=Classname("Sandy", 102)
print(C1.name)
print(C1.id)
C1.getClassname()
print(C1.getClassname())