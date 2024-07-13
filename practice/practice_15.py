def add(a, b): # def를 활용한 함수
    return a + b

add_def = add(3, 4)
print(add_def)

add_l = lambda a, b: a + b # lambda를 활용한 함수: 위 def 함수와 같은 것임

result = add_l(3, 4)
print(result)

'''---------------------------------------------------------------------------'''

a = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b, lambda a, b: a / b]
# 람다 함수는 리스트에 담아서 사용할 수도 있음
print(a[0](2, 4))
print(a[3](5, 2))
print(a[1](1, 6))