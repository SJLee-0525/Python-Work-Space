def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): #isdigit()함수는 리스트에 사용 불가능 하기에 슬라이싱을 단독으로 하였음
            print(log.split()[1])
            digits.append(log)
        else: #isalpah()
            print(log.split()[1])
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) 
    #식별자를 제외한 문자열 [1:]를 우선순위로 하며, 동일한 경우 후순위로 식별자[0]을 통해 정렬하도록 함
    return letters + digits

logs = ['dig1 8 1 8 5', 'let1 art can', 'dig2 3 6', 'let2 on kit dig', 'let3 art zero']

print(reorderLogFiles(logs))