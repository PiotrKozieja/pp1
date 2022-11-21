file = open('countries.txt','r',encoding = "utf-8")
i = 1
for line in file:
    print(i, line, end=" ")
    i = i +1
file.close()
