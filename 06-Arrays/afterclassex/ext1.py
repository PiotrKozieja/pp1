def f(n1,n2,n3):
    b = n1
    s = n1
    if n2 > b:
        b = n2
    if n3 > b:
        b = n3
    if n2 < s:
        s = n2
    if n3 < s:
        s = n3
    return(b-s)

print(f(7,4,9))
    