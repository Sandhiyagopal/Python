age=int(input("Enter the age:"))

class GetMarry(Exception):
    def __init__(self,arg):
        self.msg=arg
try:
    if age>24:
        print("Eligible")
    else:
        raise GetMarry("Not Eligible")
    
except GetMarry as xyz:
    print(xyz)