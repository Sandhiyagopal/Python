num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
for number in range(num1,num2):
    if number>1:
        for x in range(2,number):
            if(number%x)==0:
                break
        else:
           print(number)