x = [[1,2,3,4],[5,6,7,8]]

for j in range(len(x)):
    if j == 0:
        print("-"*(len(x[1])*4+1))
    print("| ",end ="")
    for i in x[j]:

        print(i, end =" | ")
    print()
    print("-"*(len(x[1])*4+1))


    
