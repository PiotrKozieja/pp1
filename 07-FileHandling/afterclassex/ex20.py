import random
f = open("ex20file.txt", "w")
for i in range(50):
    r = str(random.randint(100,999))
    f.write(r+"\n")
f.close()