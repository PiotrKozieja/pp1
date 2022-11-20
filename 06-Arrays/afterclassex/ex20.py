def star(n):
    arr = [12, 6, 4, 9, 10]
    m =0
    for i in arr:
        if m < n:
            print(f"{i}:","*"*i)
            m = m  +1
        
star(8)