import sys

N, D, K, C = map(int, sys.stdin.readline().split())
# N: 접시 수, D: 초밥 가짓 수, K: 연속해서 먹는 접시 수, C: 쿠폰 번호

# 접시 배열 입력 받기
plates = [0] * N
for n in range(N):
    plates[n] = int(sys.stdin.readline())

# 현재 먹을 수 있는 초밥의 번호를 인덱스로, 개수를 값으로 하는 초기 배열 생성
kind = [0] * (D + 1)
kind[C] = 1 # 연속해서 먹을 경우만 생각할 거니까, 쿠폰에 있는 초밥 번호 넣어주고 시작

result = 1  # 쿠폰 초밥은 항상 먹으니 1 잡아주고 시작

# 초기 값 생성
for k in range(K):
    if not kind[plates[k]]: # 만약 해당 인덱스에 값이 없다면 (0이라면)
        result += 1         # result 값 증가 (가짓 수 늚)
    kind[plates[k]] += 1    # 해당 초밥 번호의 인덱스에 값 추가

# 슬라이딩 윈도우
temp = result   # 임시 값 할당하고 시작
for start in range(1, N):           # 처음은 제외하고 순회 (초기값 생성에서 이미 함)
    kind[plates[start - 1]] -= 1    # start - 1은 연속된 초밥에서 빠져나가니까 초밥 개수에서 1 빼줌
    if not kind[plates[start - 1]]: # 감소된 값이 0이라면
        temp -= 1                   # 가짓수 감소

    if not kind[plates[(start + K - 1) % N]]:  # start를 기준으로 (K - 1)를 더한 위치의 초밥은 추가되는 초밥임: 만약 값이 없다면
        temp += 1                              # 가짓수 증가
    kind[plates[(start + K - 1) % N]] += 1     # 해당 초밥 개수 카운트

    # print(start, plates[start], temp, kind)
    result = max(result, temp)                 # 매 반복마다 최대값 갱신

print(result)