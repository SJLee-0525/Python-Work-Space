class FourCal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        result = self.x + self.y
        return result
    
    def min(self):
        result = self.x - self.y
        return result
    
    def mul(self):
        result = self.x * self.y
        return result
    
    def mod(self):
        result = self.x / self.y
        return result
    
class ThreeFourCal(FourCal):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def add_3(self):
        result = self.x + self.y + self.z
        return result

test_1 = FourCal(3, 4)
print(test_1.add())
print(test_1.min())
print(test_1.mul())
print(test_1.mod())

print()

test_2 = FourCal(5, 3)
print(test_2.add())
print(test_2.min())
print(test_2.mul())
print(test_2.mod())

print()

test_3 = ThreeFourCal(3, 5, 2)
print(test_3.z)
print(test_3.add_3())
print(test_3.add())
print(test_3.mul())