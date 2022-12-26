class Phone:
    
    def __init__(self):
        self.pstate = False
        self.vstate = 0
        self.cstate = False
    def pb(self):
        self.pstate = not self.pstate
        print("Action:Power button")
    def cb(self):
        if self.pstate == True:
            self.cstate = not self.cstate
            print("Action:Connection button")
        else:
            print("First turn on phone")
    def vstateup(self):
        if self.pstate == True:
            if self.vstate <10:
                self.vstate +=1
        else:
            print("First turn on phone")
        print("Action:Volume up")
    def vstatedown(self):
        if self.pstate == True:
            if self.vstate >1:
                self.vstate -=1
        else:
            print("First turn on phone")
        print("Action:Volume down")
    def __str__(self):
        return(f"Power state: {self.pstate}\nVolume state: {self.vstate}\nCstate: {self.cstate}")

phone = Phone()
print(phone)
print()
phone.pb()
phone.vstateup()
phone.vstateup()
phone.vstateup()
phone.vstateup()

phone.cb()
print()
print(phone)




    