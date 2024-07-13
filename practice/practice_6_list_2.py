from random import *

comment_list = list(range(1, 21))

shuffle(comment_list)
prize = sample(comment_list, 4)

# chicken = comment_list.pop()
# coffee = sample(comment_list, 3)

chicken = prize[0]
coffee = prize[1:]

print('''-- 당첨자 발표 --
치킨 당첨자 : {}
커피 당첨자 : {}
-- 축하합니다 --'''.format(chicken, coffee))