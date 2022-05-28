num1=int(input("Enter the starting number:"))
num2=int(input("Enter the Ending number:"))
for x in range(num1,num2):
    prime=True
    for y in range(2,x):
        if x%y==0:
            prime=False
    if prime==True:
        print(x)