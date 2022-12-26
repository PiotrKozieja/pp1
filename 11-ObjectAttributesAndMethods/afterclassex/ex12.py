class Point():
    
    def __init__(self,x,y,x1,y1):
        self.x = x
        import math
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.distance = math.sqrt(((x1-x)**2)+((y1-y)**2))
    def __str__(self):
        if self.distance == 0:
            return "Points are the same"
        return f'P(x:{self.x}, y:{self.y})\nP1(x1:{self.x1}, y1:{self.y1})\nDistance:{self.distance}'
e1 = Point(4,4,2,2)
print(e1)