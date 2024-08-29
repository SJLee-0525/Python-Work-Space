b = {'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for tc in range(1, T + 1):
    N, hex_num = input().split()
    result = []
    for n in hex_num: # 문자열로 입력받은 16진수를 순회
        if n.isdigit(): # 만약 숫자면
            n = int(n)  # int로 전환해 주고
            temp = ['0', '0', '0', '0']
            i = 3         # 초기 index 값
            while n != 0: # 2진수로 변환
                temp[i] = str(n % 2) # 스트링으로 넣어서 나중에 join할 수 있겍끔
                n //= 2
                i -= 1    # index 조정
            result.append(''.join(temp)) # 합쳐서 결과 리스트에 append

        else:
            result.append(b[n]) # 숫자가 아니면 b 딕셔너리에서 값 반환받아 result에 cnrk

    print(f'#{tc} {"".join(result)}') # 합쳐서 출력

