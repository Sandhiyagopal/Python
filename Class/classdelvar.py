class Person:
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        print("Should avoid one var")
    def getPerson(self):
        print("Delete the var or methods")

c=Person(20,30,40)
del c.p1
print(c.p1)