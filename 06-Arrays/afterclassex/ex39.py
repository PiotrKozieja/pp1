arr =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range((len(arr[0]))):
        arr[0][i] = i+1
for i in range(1,len(arr)):   ###wykoannie instrukcji dla pieciurzedow
    for j in range(len(arr[i])):   ##wyoknanie dla poszczegolnych sekcji
        arr[i][j] = (arr[0][j])*(i+1)

##printing
for i in range(len(arr)):
    for j in arr[i]:
        print(j, end =" ")
    print()
    

    
