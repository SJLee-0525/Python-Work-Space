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
    for w in x:
        temp[''.join(sorted(w))].append(w) 
        # 정렬해서 같은 형식이 되도록 해 key에 추가하고, 원본 값을 value에 append함
    return dict(temp)

ana = anagrams(word)

for a, b in ana.items():
    print(f'{a}는 {b}')

# aet는 ['eat', 'tea', 'ate']
# ant는 ['tan', 'nat']
# abt는 ['bat']