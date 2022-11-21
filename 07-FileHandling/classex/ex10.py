f = open("myfile.txt", "w")
arr = ["Piotr","Kozieja","UEK","IS"]
for i in arr:
    f.write(i+"\n")
f.close()

