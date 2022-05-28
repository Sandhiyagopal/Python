def fun(num):
    a= list(num)
    b=a[slice(-5,-1)]
    for x in b:
        print(x,end="")
    
fun("444444444444444")