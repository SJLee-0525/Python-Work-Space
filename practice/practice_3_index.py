jumin = '031111-1234567'

f_num = int(jumin[7])
birth_y = int(jumin[:2])
birth_m = int(jumin[2:4])
birth_d = int(jumin[4:6])

if f_num % 2 == 1:
    print('성별: 남자')
    if 0 <= birth_y < 10:
        print(f'200{birth_y}년 {birth_m}월 {birth_d}일생')
    elif 10 <= birth_y < 30:
        print(f'20{birth_y}년 {birth_m}월 {birth_d}일생')
    else:
        print(f'19{birth_y}년 {birth_m}월 {birth_d}일생')
else:
    print('성별: 여자')
    if 0 <= birth_y < 10:
        print(f'200{birth_y}년 {birth_m}월 {birth_d}일생')
    elif 10 <= birth_y < 30:
        print(f'20{birth_y}년 {birth_m}월 {birth_d}일생')
    else:
        print(f'19{birth_y}년 {birth_m}월 {birth_d}일생')

print(f'주민번호 뒷자리: {jumin[-7:]}')