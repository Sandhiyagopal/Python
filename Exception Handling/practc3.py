age=input("Enter the your age:")
try:
    if age<25:
        print("your not eligiblie")
    else:
        raise("you are not eligible for college")
except:
    print("your Eligible")
