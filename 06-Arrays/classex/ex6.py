
arr = [2,3,7,5,4]
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[len(arr)-1])
print(arr[len(arr)-2])
print(int(arr[0]+ int(arr[len(arr)-1])))
print(int(arr[1])+int(arr[2])+int(arr[3]))
for i in range(len(arr)):
    print(arr[i],end = " ")
print()

for i in range(len(arr)-2):
    print(arr[i],end = " ")
print()


    ###########
# zapis (liczba przedostatnia) === arr[len(arr)-1] === arr[-1]---liczy od tylu
#middle value
print("LEN",arr[len(arr)//2])