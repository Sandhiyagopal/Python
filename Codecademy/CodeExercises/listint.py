def fun(arg):
    print(arg)
    
l1=[20,11,"sandy",44,49,30,"gopal",78,"Hi"]
fun(l1)

l2=[]
for x in l1:
    if type(x)==int:
        l2.append(x)
print(l2)

