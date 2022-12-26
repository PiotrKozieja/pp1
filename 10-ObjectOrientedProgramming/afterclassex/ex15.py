class thermometer:
    def __init__(self):
        self.temp = 0
        self.s = 0
    def ton(self):
        self.s = 1
    def toff(self):
        self.s=0
        self.temp = 0
    def tch(self,temp):
        self.temp = temp
        if self.s == 1:
            if self.temp <34 or self.temp>42:
                print("out of range")
            else:
                print(self.temp, " ")
                if self.temp > 37 and self.temp <41:
                    print("fever")
                if self.temp >= 41:
                    print("Critical")
        else:
            print("thermometer is off")

        


    

    

