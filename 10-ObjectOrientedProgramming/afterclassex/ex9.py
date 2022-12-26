class TV:
    def __init__(self):
        self.boolean = False
        self.c = 1
    def turn_on(self):
        self.boolean = True
    def turn_off(self):
        self.boolean = False
    def show_status(self):
        if self.boolean == True:
            print("ON")
        else:
            print("OFF")
        print("Channel",self.c)
    def c_up(self):
        if self.boolean>0:
            self.c +=1
    def c_down(self):
        if self.boolean>0 and self.c >=2:
            self.c -=1
TV = TV()
TV.show_status()
TV.turn_on()
TV.c_up()
TV.show_status()
TV.turn_off()
TV.c_up()
TV.show_status()
TV.turn_on()
TV.c_down()
TV.c_down()
TV.show_status()
TV.c_down()
TV.show_status()
