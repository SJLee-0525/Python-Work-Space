# my_list = list(map(int, input().split()))
# or_list = [1, 1, 2, 2, 2, 8]
# buy_list = []

# for i in range(len(or_list)):
#     print(or_list[i] - my_list[i], end = ' ')

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")