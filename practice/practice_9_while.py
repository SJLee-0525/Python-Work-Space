# customer = '토르'
# i = 5

# while i >= 1:
#     print('{0}님 커피가 준비되었습니다. {1}번 남았어요.'.format(customer, i))
#     i -= 1

#     if i == 0:
#         print('오늘 커피가 다 소진되었습니다.')


customer = '아이언맨'
person = 'Unknown'

while True:
    print('커피가 준비되었습니다.')
    person = input('이름이 어떻게 되세요?')

    if customer == person:
        print('감사합니다. 또 오세요.')
        break