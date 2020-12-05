class Equality():
    def __init__(self, x=180):
        self.x=x
    def check(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a+self.b+self.c==self.x)

x1=Equality()
x1.check(60, 60, 60)
