# 비밀번호 생성기

url = "http://samsung.com"

cut_url = url.replace('http://', '')
cut_url = cut_url[:cut_url.index('.')]
print(cut_url)

pw = cut_url[:3] + str(len(cut_url)) + str(cut_url.count('e')) + '!'

print('{site}의 비밀번호는 {pw}입니다.'.format(site = url, pw = pw))