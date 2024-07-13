try:
    age = int(input())

except:
    print('입력이 정확하지 않습니다.')

else: # 오류가 발생하지 않았을 때 시행될 구문
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다')