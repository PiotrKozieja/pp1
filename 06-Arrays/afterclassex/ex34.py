def f(x,y):
    sum = 0
    for i in x:
        if y.count(i) == 0:
            sum = sum +1
    if sum == 0:
        return(True)
    else:
        return(False)
    




print(f([1,2,11],[1,2,3,4,5,6,7,10]))