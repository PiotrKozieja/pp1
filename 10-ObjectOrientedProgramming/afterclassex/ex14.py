class ebook:
    def __init__(self,book,author,nop):
        self.nop = nop
        self.author = author
        self.book = book
        self.nop = nop
        self.apn = 1
        self.os = 0
    def open(self):
        self.os = 1

    def close(self):
        self.os = 0

    def np(self):
        if self.apn <self.nop and self.os == 1:
            self.apn +=1

    def pp(self):
        if self.apn>=2 and self.os == 1:
            self.apn-=1
    def show_status(self):
        print(self.book,self.author,self.nop,self.apn)
awk =ebook("Alicja w Krainie","JKR",3)
awk.show_status()
awk.np()
awk.np()
awk.show_status()
awk.open()
awk.pp()
awk.pp()
awk.pp()
awk.pp()
awk.show_status()
awk.np()
awk.np()
awk.np()
awk.np()
awk.show_status()

