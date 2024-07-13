class FourCal:
    def __init__(self, first, second): # 생성자: 아까의 setdata 과정이 없어짐. 객체가 호출될 때 자동으로  호출되는 매서드
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    

a = FourCal(4, 3)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal): # 클래스의 상속: class 새 클래스 명 (부모 클래스)
    def pow(self):  # 새 클래스에 새로운 기능을 넣지 않았는데도
       result = self.first ** self.second
       return result

b = MoreFourCal(5, 3) # 잘 작동함 (상속됐기 때문)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print(b.pow()) # 자식 클래스에 새로 추가된 기능

class SafeFourCal(MoreFourCal):
    def div(self): # 부모의 div 클래스를 덮어 씌움 (부모 클래스를 바꾸는 것은 아니고, 현재 클래스에 덮어씌움) = 매서드 오버라이딩
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
c = SafeFourCal(5, 0) 
print(c.add())
print(c.sub())
print(c.mul())
print(c.div()) # 원래의 부모 클래스였다면 0으로 나눌 경우 오류가 났을 것임
print(c.pow())