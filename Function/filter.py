//method 1
print(list(filter(lambda num:num%2==0, range(1,21))))
//method 2
l1=[2,4,11,44,83,95,14,8,33]
def even(x):
    if x%2==0:
        return True
    else:
        return False
    
l2=list(filter(even,l1))
print(l2)