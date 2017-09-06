class SuperClass:
    def printX(self):
        self.x = 10
        print(self.x)

class SubClass(SuperClass):
    y = 10
    def printY(self):
        print(self.y)
    def __add__(self, sub2):
        self.y += sub2.y
        return self

s = SubClass()
s.a = 30

s2 = SubClass()
s2.y = 30

s2 += s


s2.printY()