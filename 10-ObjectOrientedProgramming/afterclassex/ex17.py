class number:
    def __init__(self):
        self.arr = []
        self.arr1 = self.arr
        self.arr1.sort()
        self.sum = 0
        self.arr2 = []
        
    def add(self,n):
        for k in n:
            self.arr.append(k)
        for i in self.arr1:
            self.sum += i
        
        for j in self.arr:
            j = str(j)
            self.arr2.append(j)
    def greatest(self):       
        print(self.arr1[-1])
    def smallest(self):
        print(self.arr1[0])
    def arithmetic(self):
        print(self.sum/len(self.arr))
    def suma(self):
        print(self.sum) 
    def display(self):
        print(", ".join(self.arr2))
    def median(self):
        if len(self.arr1)%2 != 0:
            print(self.arr1[len(self.arr1)//2])
        else:
            print((self.arr1[len(self.arr1)//2-1]+self.arr1[len(self.arr1)//2])/2)

f = number()
f.add([1,2,3,4])
f.greatest()
f.smallest()
f.display()
f.suma()
f.arithmetic()
f.median()
print()
g = number()
g.add([1,2,3,4,5])
g.greatest()
g.smallest()
g.display()
g.suma()
g.arithmetic()
g.median()
print()
h = number()
h.add([5,4,3,2,1])
h.greatest()
h.smallest()
h.display()
h.suma()
h.arithmetic()
h.median()


        

