'''
문자열 배열을 받아 애너그램 단위로 그루핑하라
'''

from collections import *

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# def anagrams(input_words):
#     temp = defaultdict(list) 
#     # 존재하지 않는 키를 삽입하려 할 경우 KeyError가 발생하는데, 일르 방지하기 위해 항상 디폴트를 생성해주는 defaultdict() 선언

#     for word in input_words:
#         temp[''.join(sorted(word))].append(word) 
#         # w를 sorted 하면 리스트 형태로 반환, 그것을 다시 문자열로 만들기 위해 .join 사용
#         # 정렬해서 같은 형식이 되도록 해 key에 추가하고, 원본 값을 value에 append함

#     return dict(temp)

def anagrams_2(words):
    word_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in word_dict:
            word_dict[sorted_word] = [word]
        else:
            word_dict[sorted_word].append(word)

    return word_dict
    

ana = anagrams_2(words)

for sorted_word, word in ana.items():
    print(f'{sorted_word}는 {word}')

# aet는 ['eat', 'tea', 'ate']
# ant는 ['tan', 'nat']
# abt는 ['bat']