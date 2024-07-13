f = open("C:/Users/sungj/Desktop/Python Work Space/practice/새파일.txt", "w", encoding = "UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 'w'는 쓰기, 'r'는 읽기, 'a'는 추가