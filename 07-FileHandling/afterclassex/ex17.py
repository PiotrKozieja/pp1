f = open("examplefile.txt", "r")
for line in f:
    i = open("copylines.txt", "a")
    i.write(line)
i.close()
f.close()