def f(x):
    s = x[0][0]
    b = x[0][0]

    for i in range(len(x)):
        for j in x[i]:
            if j <= s:
                s =j
                s1 = i
            if j >= b:
                b = j
                b1 = i
    lb1= x[b1].index(b)+1
    lb2 =(x.index(x[b1])+1)

    ls1= x[s1].index(s)+1
    ls2 = (x.index(x[s1])+1)

    return("location biggest:",lb1,lb2, "Location smallest", ls1,ls2)

    


print(f([[-38, 19], [5,40],[-7,11],[29,16]]))