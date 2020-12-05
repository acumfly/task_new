class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def chek_sum(self):
        if self.a+self.b+self.c==180:
            print("triangle")
        else:
            print("It's not a triangle")
x=Triangle(25, 21, 34)
x.chek_sum()
