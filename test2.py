class Equality():
    def __init__(self, x):
        self.x=x
    def check(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a+self.b+self.c==self.x)


x1=Equality(67)
x1.check(30, 30, 7)
