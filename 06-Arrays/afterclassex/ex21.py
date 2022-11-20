def f(array1, array2):
    sum = 0
    if len(array1)==(len(array2)):
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                sum = sum+1
                
    else:
        sum = sum+1
    print(sum == 0)





f(["water","book","sky"],["water","book","sky"])