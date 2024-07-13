f = open("C:/Users/sungj/Desktop/Python Work Space/practice/새파일.txt", 'r', encoding = "UTF-8")

while 1:
    line = f. readline() # readline()은 한 줄씩 읽는 함수임
    if not line:
        break
    print(line, end = '')

''' -------------------------------------------------------------------------- '''

# lines = f.readlines() #readlines()는 각각의 줄을 리스트 형태로 전체를 가져옴
# for line_1 in lines:
#     print(line_1.strip())

''' -------------------------------------------------------------------------- '''

# for line2 in f: # for문을 활용해 함수 없이 전체 읽기
#     print(line2, end='')

# data = f.read() # .read()는 통째로 다 갖고 옴
# print(data)

f.close



