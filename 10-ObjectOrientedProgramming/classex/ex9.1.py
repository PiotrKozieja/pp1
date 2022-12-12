class  TV():
    def __init__(self):
        self.is_on =False
        self.n = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f"Tv is on, Channel {self.n}")
        else:
            print("Tv is off")
    def set_c(self, n):
        self.n = n
        
tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.set_c(5)
tv1.show_status()
