class  TV():
    def __init__(self):
        self.is_on =False
        self.c  = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print("Tv is on")
            print(self.c)
        else:
            print("Tv is off")
    def c_up(self):
        if self.is_on:
            self.c+=1
    def c_down(self):
        if self.is_on:
            self.c-=1

tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.c_up()
tv1.show_status()

