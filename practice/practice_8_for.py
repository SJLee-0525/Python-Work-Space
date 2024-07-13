# starbucks = ['아이언맨', '토르', '스파이더맨', '아이엠 그루트']

# for customer in starbucks:
#     print(f'{customer}님 커피가 준비되었습니다.')

'''한 줄 for'''

# 1동을 101동으로, 2동을 102동으로

# apartment = range(1, 15)

# apartment = [i + 100 for i in apartment]
# print(apartment)

# 학생 이름을 길이로 변환

# students = ['Sungjoon', 'Iron man', 'I am groot']

# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환

students = ['Sungjoon', 'Iron man', 'I am groot']

students = [i.upper() for i in students]
print(students)