from sys import *

n = int(input())

stu_list = list(map(int, stdin.readline().split()))

final_list = []
temp_list = []
temp_n = n
target = 1

while 1:
    print(final_list)
    print(temp_list)
    if stu_list[0] == target:
        temp = stu_list.pop(0)
        final_list.append(temp)
        target += 1

    elif stu_list[0] == temp_n:
        temp = stu_list.pop(0)
        temp_list.append(temp)
        temp_n -= 1

    elif temp_list[-1] == target:
        temp = temp_list.pop()
        final_list.append(temp)
        target += 1
    
if len(final_list) == n:
    print('Nice')
    
    
elif len(final_list) != n:
    print('Sad')
    

# if target == n:
#     print('Nice')
#     break

# elif target != n:
#     print('Sad')
#     break
    
    # print(stu_list)
    
    #     if len(temp_list) == 0 and len(stu_list) == 0:
    #         print('Nice')
        






# while 1:
#     if temp_list[-1] == num:
#         temp_2 = temp_list.pop()
#         final_list.append(temp_2)
#         num += 1

#     if len(temp_list) == 0:
#         print('Nice')
#         break

#     else:
#         break
   