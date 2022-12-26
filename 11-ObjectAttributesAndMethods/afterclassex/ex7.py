class student():
    id = 1000
    def __init__(self, name):
        self.name = name
        self.university = "Uek"
        self.field = "Math"
        self.id = student.id
        student.id+=1
    def __str__(self):
        return(f"Name: {self.name}\nField:{self.field}\nU:{self.university}\nId:{self.id}")
s1 = student("Johnny Depp")
print(s1)
s2 = student("Amber Heard")
print(s2)
s3 = student("Kate Moss")
print(s3)


