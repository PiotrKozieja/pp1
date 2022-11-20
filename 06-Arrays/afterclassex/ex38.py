def f(x,y):
    for j in range(y):
        print("-"*((x)*4+1))
        for i in range(x):
            if i == 0:
                print("|",end=" ")
            print(" ", end =" | ")
        print() 
        print("-"*((x)*4+1))


    

f(10,5)