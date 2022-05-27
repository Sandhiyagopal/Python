def fun(arg):
    x=list(arg)
    a_count=x.count("a")
    e_count=x.count("e")
    i_count=x.count("i")
    o_count=x.count("o")
    u_count=x.count("u")
    total=a_count+e_count+i_count+u_count+o_count
    print(total)
    print(f"Total vowels present in your name: {total}\n 'A' count is {a_count}\n 'E' count is {e_count}\n 'I' count is {i_count}\n 'O' count is {o_count}\n 'U' count is {u_count}")
    
fun("sandhiya")