def f(x):
    sum = int(x[0])
    for i in range(len(x)):
        if x[i] == "+":
            sum = sum +int(x[i+1])
        if x[i] == "-":
            sum = sum -int(x[i+1])

    print(sum)
f("3-8+1")
        
