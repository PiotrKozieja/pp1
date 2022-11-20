def f(n):
    exit = n[0]
    for i in range(len(n)):
        if n[i] == " ":
            exit = exit +(n[i+1])
    print(exit)
f("game of trone")