def f(x):
    sum = 0
    for i in range(len(x)):
        if x[i] != x[-i-1]:
            sum = sum +1
    return(sum == 0)
print(f("abccba"))
