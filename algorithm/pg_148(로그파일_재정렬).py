'''
로그를 재정렬하라. 기준은 아래와 같다
    1. 로그의 가장 앞 부분은 식별자다
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
    4. 숫자 로그는 입력 순서대로 한다.
'''

def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        #isdigit()함수는 리스트에 사용 불가능 하기에 슬라이싱을 단독으로 하였음
        if log.split()[1].isdigit(): # 만약 log의 두번째 문자열이 숫자면?
            print(log.split()[1])
            digits.append(log)
        else: # == isalpah()
            print(log.split()[1])
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
    #식별자를 제외한 문자열 [1:]를 우선순위로 하며, 동일한 경우 후순위로 식별자[0]을 통해 정렬하도록 함
    return letters + digits

logs = ['dig1 8 1 8 5', 'let1 art can', 'dig2 3 6', 'let2 on kit dig', 'let3 art zero']

print(reorderLogFiles(logs))