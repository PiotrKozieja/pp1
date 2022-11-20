def f(x):
    arr = []  
    for i in range(x):
        arr.append([])
        for j in range (x):
            if i == j:
                arr[i].append(1)
            else:
                arr[i].append(0)

    for i in arr:
        print(i)
        
f(5)