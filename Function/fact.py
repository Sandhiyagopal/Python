def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
print(fact(4))

def fact(n):
    i=1
    while n>=1:
        i=i*n
        n=n-1
    return i
result=fact(5)
print(result)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
