num=int(input("Enter the number:"))
i=1
while i<=num:
    if num%i==0:
        print(i)
    i=i+1
    
num2=int(input("Enter the number2:"))
for x in range(1, num2+1):
    if num2%x==0:
        print(x)
        