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
    def c_channel(self, setchannel):
        if self.boolean == True:
            self.c = setchannel

tv = TV()
tv.show_status()
tv.turn_on()
tv.c_channel(5)
tv.show_status()
tv.c_channel(1)
tv.show_status()
tv.turn_off()
tv.show_status()
tv.c_channel(5)
tv.show_status()
tv.turn_on()
tv.c_channel(5)
tv.show_status()




