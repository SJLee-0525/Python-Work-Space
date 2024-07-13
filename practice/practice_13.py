def add(a, b):
    return a + b

print(add(1, 2))

'''---------------------------------------------------------------------------'''

def say(): #입력 값이 없음.
    return 'Hi'

print(say())

'''---------------------------------------------------------------------------'''

def add2(a, b):
    print(f'{a}, {b}의 합은 {a + b}입니다.')

a = add2(1, 3)
print(a) #출력 값이 없음.

'''---------------------------------------------------------------------------'''

def sub(a, b):
    return a - b

result = sub(b = 6, a = 2) #매개 변수를 지정해서 사용할 수도 있음
print(result) 

'''---------------------------------------------------------------------------'''

def add_many(*args): # *을 붙이면 입력 값을 전부 모아 튜플로 만들어주기 때문에, 매개 변수의 개수를 지정할 필요가 없어짐. 
    result = 0
    for i in args:
        result += i
    return result

z = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(z)

'''---------------------------------------------------------------------------'''

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

x = add_mul('add', 1, 2, 3, 4, 5)
y = add_mul('mul', 1, 2, 3, 4, 5)
print(x, y)

'''---------------------------------------------------------------------------'''

def print_kwargs(**kwargs): # 입력을 키: 워드 형태 (dict) 로 받겠다는 뜻
    print(kwargs)

print_kwargs(a = 1, b = 2 , c = 3)

'''---------------------------------------------------------------------------'''

def say_nick(nick): 
    if nick == "바보": 
        return # 리턴을 활용해 특정 조건에서 함수를 강제 종료시킬 수 있음
    print("나의 별명은 %s 입니다." % nick)

say_nick('성준')
say_nick('바보')
say_nick('스파르타')

'''---------------------------------------------------------------------------'''

def say_myself(name, old, man = True): # 초기값을 사용하고 싶은 변수는 무조건 맨 뒤에 두어야 함함
    print('나의 이름은 %s 입니다.' % name)
    print('나의 나이는 %s살 입니다.' % old)
    if man:
        print('나는 남자입니다.') 
    else:
        print('나는 여자입니다.')

say_myself('싸피', 12) # 초기값을 지정했기 떄문에, 값을 입력하지 않았음에도 남자로 입력됨
say_myself('SSAFY', 13, 0) # True가 아닐때: False일 떄 여자로 출력하도록 설정해 뒀으므로 0을 입력해도 False로 인식했음.
