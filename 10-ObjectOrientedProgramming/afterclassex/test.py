class test:
    def __init__(self):
        self.number =1
    def inc(self,x):
        self.number += x
    def show(self):
        print(self.number)
f = test()
f.inc(5)
f.show()
