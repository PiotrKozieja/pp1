f = open("ex21file.txt", "w")
for i in range(1,11):
    for j in range(1,4):
        f.write(str(i**j)+" ")
    f.write("\n")