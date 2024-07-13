f = open("C:/Users/sungj/Desktop/Python Work Space/practice/새파일.txt", 'a', encoding = 'UTF-8')

for i in range(11, 20):
    data = '%s번째 줄입니다.\n' % i
    f.write(data)

f.close()