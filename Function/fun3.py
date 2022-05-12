def cal(a,b=10):
    return a-b

print(cal(10))
print(cal(10,20))


def cal(x,y):
    sum = x+y
    sub = x-y
    multi=x*y
    return sum,sub,multi

print(cal(10,20))
r1=cal(21,31)
print(r1)