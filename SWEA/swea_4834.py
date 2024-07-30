T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 카드 장수
    card_list = list(map(int, input()))

    # 카드 리스트에서 최대 값 찾기
    max_value = card_list[0]
    for value in card_list:
        if max_value < value:
            max_value = value

    # 카드 번호를 인덱스로, 개수를 값으로 하는 리스트 생성
    counts = [0] * (max_value + 1)
    for card_num in card_list:
        counts[card_num] += 1

    # counts 리스트 내에서 최대 값 찾기
    # 만약 값이 크거나 같다면 인덱스 번호를 이용해 카드 번호 갱신
    max_i = counts[0]
    max_card = 0
    for card_num, i in enumerate(counts):
        if max_i <= i:
            max_i = i
            max_card = card_num

    print(f'#{test_case} {max_card} {max_i}')