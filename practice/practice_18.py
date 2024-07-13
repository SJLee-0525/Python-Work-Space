class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first = self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal() # FourCal.setdata(a, 4, 2) 와 같음
a.setdata(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

b = FourCal()
b.setdata(1, 3)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())


