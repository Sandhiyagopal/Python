try:
  print(10/0)
except ValueError as err1:
    print(err1)
except ZeroDivisionError as err2:
    print(err2)