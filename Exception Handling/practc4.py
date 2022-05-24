try:
    f=open("abc.txt")
    data=f.read()
    print(data)
except:
    f=open("abc1.txt", 'w')
    data=f.writer()
    data.writerow("Eno", "Ename")
    print(data)