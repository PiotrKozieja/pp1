f= open("ex19file.txt", "w")
for i in range(50):
    i = str(i+1)
    f.write(i+"\n")
f.close()