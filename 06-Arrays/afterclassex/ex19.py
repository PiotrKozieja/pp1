arr = [15, 8, 31, 47, 2, 19]
sum = 0
n=0
while True:

    i = arr[n]
    sum = sum + i
    n=n+1
    if n ==6:
        break
print(sum)
print(len(arr))
print("arithmetic mean:",sum/len(arr) )