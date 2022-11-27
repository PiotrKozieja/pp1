def f(x):
    f = open(x, "r")
    sum = 0
    for i in f:
        sum = sum + 1
    print(x)
    print("lines", sum)
f("filename.txt")


