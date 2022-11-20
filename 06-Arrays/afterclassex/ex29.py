def f(x,y):
    x1 = []
    for i in x:
        if i > y:
            x1.append(i)
            
    print("".join(x1))



f([1,2,3,4,5,6,7,8,9],5)