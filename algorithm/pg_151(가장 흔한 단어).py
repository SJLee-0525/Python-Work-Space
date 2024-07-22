'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
'''

def mostCommonWord(sentence, banned_list):
    word_list = sentence.split()

    new_words_list = []
    for word in word_list:
        word = list(word)
        new_word_list = []
        for w in word:
            if w.isalpha() == True:
                new_word_list.append(w)
        new_word = ''.join(new_word_list).lower().strip()
        new_words_list.append(new_word)

    word_dict = {}
    for new_word in new_words_list:
        if new_word not in banned_list:
            if new_word not in word_dict:
                word_dict[new_word] = 1
            else:
                word_dict[new_word] = word_dict[new_word] + 1

    result = max(word_dict, key=word_dict.get)
    return result

paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit'
banned = ['hit']

result = mostCommonWord(paragraph, banned)
print(result)
