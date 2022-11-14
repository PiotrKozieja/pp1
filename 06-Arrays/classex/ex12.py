x =[[2,5,4],[9,0,3]]
print(x)
######
sum = 0
for i in x:
    sum = sum + len(i)
print("sum", sum)
print(len(x))
print(len(i))
#########
print(x[1][1])
#########
print(x[1][2])
#########
print(x[1])
print()
#########
for i in x:
    for j in i:
        print(j,end = " ")
    print()
print()
########
for i in x:
    print(i[len(i)-1])