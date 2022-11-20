def f(x):

    for k in range(2):
        for i in range(len(x)):
            for j in x[i]:
                print(j, end =" ")
            print()
        for i in range(len(x)):
            x0 =x[i][0]
            xl = x[i][-1]
            x[i][0] = xl
            x[i][-1] = x0
        print()



print(f([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]))