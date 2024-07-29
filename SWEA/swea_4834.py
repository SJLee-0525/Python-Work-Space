T = int(input())

for test in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, list(input())))

    card_dict = {}
    for target in card_list:
        count = 0
        for card in card_list:
            if target == card:
                count += 1
    
        if count not in card_dict:
            card_dict[count] = [target]
        else:
            if target not in card_dict[count]:
                card_dict[count].append(target)
    
    card_counts_key = list(card_dict.keys())
    
    max_key = card_counts_key[0]
    for card_key in card_counts_key:
        if max_key < card_key:
            max_key = card_key
    
    final_value_list = card_dict[max_key]

    max_value = final_value_list[0]
    for final_value in final_value_list:
        if max_value < final_value:
            max_value = final_value
    
    print(f'#{test} {max_value} {max_key}')
