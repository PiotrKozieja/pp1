class  TV():
    def __init__(self):
        self.is_on =False
        self.n = 1
        self.cn = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f"Tv is on, Channel {self.n}")
        else:
            print("Tv is off")
        print(self.cn)
    def set_c(self, n):
        self.n = n
    def addcn(self, c):
        self.cn.append(c)
        
tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.show_status()
tv1.addcn("TVP")
tv1.addcn("TVP2")
tv1.addcn("TVP3")
tv1.set_c(2)
tv1.show_status()