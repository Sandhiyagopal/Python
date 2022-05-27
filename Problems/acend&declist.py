import random
def fun(num,num2):
    if num2=="asc":
        num.sort()
        print(num)
    elif num2=="desc":
        num.sort(reverse=True)
        print(num)
    elif num2=="none":
        print(num)
    
b=random.choice(["desc","none","asc"])
fun([20,30,11,44,56,89,32],b)