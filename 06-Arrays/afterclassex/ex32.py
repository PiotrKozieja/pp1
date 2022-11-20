x = [1,2,3,4,5,6,7]
sum = ""
n = 0
for i in x:
    x1 = i
    x1 = str(x1)
    sum = sum + x1
    n= n+1
    if n< len(x):
        sum = sum + ", "
print(sum)