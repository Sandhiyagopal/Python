def prime_finder(n):
  for x in range(n):
    prime=True
    for i in range(2,x):
      if x%i==0:
        prime=False
    if prime==True:
      print(x)
     
prime_finder(11)