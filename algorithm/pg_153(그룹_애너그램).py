from collections import *

word = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# for x, y in enumerate(a + 1):
#     print(x, y)

# for i in range(len(a) + 1):
#     try:
#         print(a[i])
#     except IndexError:
#         print('x')

def anagrams(x):
    temp = defaultdict(list) 
    # 존재하지 않는 키를 삽입하려 할 경우 KeyError가 발생하는데, 일르 방지하기 위해 항상 디폴트를 생성해주는 defaultdict() 선언

    for w in x:
        temp[''.join(sorted(w))].append(w) 
        # w를 sorted 하면 리스트 형태로 반환, 그것을 다시 문자열로 만들기 위해 .join 사용
        # 정렬해서 같은 형식이 되도록 해 key에 추가하고, 원본 값을 value에 append함

    return dict(temp)

ana = anagrams(word)

for a, b in ana.items():
    print(f'{a}는 {b}')

# aet는 ['eat', 'tea', 'ate']
# ant는 ['tan', 'nat']
# abt는 ['bat']