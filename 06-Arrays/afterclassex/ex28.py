def f(x):
    med = 0
    x.sort()
    if len(x)%2 != 0:
        med = x[(len(x)//2)]
    else:
        med = ((((x[len(x)//2]-1))+(x[len(x)//2]))/2)
    print(med)
f([8,7,6,5,4,3,2,1])