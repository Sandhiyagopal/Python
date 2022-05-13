def reverse_str2(name2):
    result2=""
    r1=len(name2)
    while r1>0:
        result2=result2+name2[r1-1]
        r1=r1-1
    return result2
name2="Sandhiya Gopal"
print(reverse_str2(name2))

