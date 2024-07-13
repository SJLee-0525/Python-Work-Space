#input은 항상 str으로 받기 때문에 숫자를 원한다면 int/float로 변환시켜야 함

temp = int(input('오늘 기온은?'))

if temp >= 30:
    print('너무 더워요. 나가지 마세요.')
elif 30 > temp >= 10:
    print('괜찮은 날씨에요.')
elif 10 > temp >= 0:
    print('외투를 챙기세요.')
else:
    print('너무 추워요. 나가지 마세요.')