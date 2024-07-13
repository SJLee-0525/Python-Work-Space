subway = [1, 2, 3]
people = ['유재석', '조세호', '박명수']

print(subway[2])

# 두 리스트를 사전으로 변환
print(dict(zip(subway, people)))

# 두 리스트 합치기
subway.extend(people)
print(subway)

python_set = {'유재석', '조세호', '박명수', '양세찬'}
python_set.add('노홍철')
print(python_set)