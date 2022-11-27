f = open("examplefile.txt", "r")
c= 0
while True:
    if c < 5:
        print(f.readline())
        c = c+1
    else:
        x = input("Next?")
        if x == "":
            c = 0
        if x =="b":
            break
print("End")
        
