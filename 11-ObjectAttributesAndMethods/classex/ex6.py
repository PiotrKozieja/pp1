class student():
    id = 10000
    University = "UEK"
    def __init__(self,Name,Surname):
               
        self.Name = Name
        self.Surname = Surname
        self.id = student.id
        student.id +=1
    def __str__(self):
        return(f"Name:{self.Name}\nSurname:{self.Surname}\nUniversity: {self.University}\nID:{self.id}")
studnet1 = student("abc","def")
student2 = student("jaj","bab")
print(studnet1)
print()
print(student2)


#####^^^^^^^^^^^^^^^^^
####zdjecie z 19.12.22