# result =  0 

# def calculator(num):
#     global result
#     result += num
#     return result

# print(calculator(3))
# print(calculator(8))
# print(calculator(4))



class Cal:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
cal_1 = Cal()
cal_2 = Cal()

print(cal_1.add(3))
print(cal_1.add(11))
print(cal_1.sub(2))
