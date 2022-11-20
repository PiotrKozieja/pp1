def f(arr1,arr2):
    s = 0
    arr3 = []
    for i in arr1:
        for j in arr2:
            if i == j:
                s = s + 1
        if s == 0:
            #print(i, end = " ")
            arr3.append(i)
        s = 0
    return(arr3)
print(f([4,36,12,28,9,44,5],[5,1,36]))