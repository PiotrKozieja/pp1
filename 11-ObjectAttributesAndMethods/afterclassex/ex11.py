class calc:
    def circle(self,r):
        print(f"Circle Surface:{(3.14)*(r**2)}")
    def Rectangle(self, a, b):
        print(f"Rectangle Surface:{a*b}")
    def Triangle(self,b, h):
        print(f"Triangle Surface:{(b/2)*h}")
f1 = calc()
f1.circle(2)
f1.Rectangle(5,2)
f1.Triangle(2,5)

