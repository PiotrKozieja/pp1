def f(x):
    l = len(x)
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] == x[j] and i != j:
                l = l -1
    print(l)
f("abcdeee")
