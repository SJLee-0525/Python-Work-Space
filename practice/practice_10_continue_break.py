# 결석
absent = [2, 4, 7, 11]
no_book = [8]

for student in range(1, 12):
    if student in absent:
        continue

    elif student in no_book:
        print('오늘 수업 여기까지. {}는 교무실로 따라오렴'.format(student))
        break

    print(f'{student}야 책을 읽어줘.')
