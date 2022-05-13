def secmax(list):
    list.sort()
    return list[-2]

li=[]
length=int(input("Enter the length of list:"))

for x in range(0,length):
    values=int(input("Enter the values for list:"))
    li.append(values)

print(secmax(li))