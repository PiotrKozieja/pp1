class TV:
    def __init__(self):
        self.boolean = False
        self.c = 1
        self.c_list = []
    def turn_on(self):
        self.boolean = True
    def turn_off(self):
        self.boolean = False
    def show_status(self):
        if self.boolean == True:
            print("ON")
            try:
                print("Channel",self.c,self.c_list[self.c-1])
            except:
                print("Channel",self.c)

        else:
            print("OFF")
        

    def c_channel(self, setchannel):
        if self.boolean == True:
            self.c = setchannel
    def set_channels(self,newlist):
        for i in newlist:
            self.c_list.append(i)
tv = TV()
tv.show_status()
tv.turn_on()
tv.set_channels(["t1","t2"])
tv.show_status()
tv.c_channel(2)
tv.show_status()