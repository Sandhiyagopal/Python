f=open("abc.txt",'r')

print(f.readline(5))
print(f.readlines()) #readlines will read all lines so it will convert list values.

f.close()