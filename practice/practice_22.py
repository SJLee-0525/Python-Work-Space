try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
    #pass를 활용해 오류를 회피할 수도 있음
    
# try:
#     f = open('없는 파일', 'w')
# finally: # 중간에 오류가 발생하더라도 무조건 실행됨
#     f.close()
#     print('오류')