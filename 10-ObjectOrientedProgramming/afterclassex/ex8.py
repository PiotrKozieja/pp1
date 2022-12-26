class TV:
    def __init__(self):
        self.boolean = False
    def turn_on(self):
        self.boolean = True
    def turn_off(self):
        self.boolean = False
    def show_status(self):
        print(self.boolean)
TV = TV()
TV.show_status()
TV.turn_on()
TV.show_status()
TV.turn_off()
TV.show_status()