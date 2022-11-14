x = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max = x[0]
for i in x:
    if len(i) > len(max):
        max = i
print(max)