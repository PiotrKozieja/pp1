def f(arr):
    arr1 = []
    for i in arr:
        if i%2 == 0:
            arr1.append(i)
    for i in arr:
        if i%2 != 0:
            arr1.append(i)
    return(arr1)

print(f([1,2,3,4,5,6,7,8]))