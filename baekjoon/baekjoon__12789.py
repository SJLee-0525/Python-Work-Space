import sys
from collections import deque

n = int(sys.stdin.readline().strip())

stu_list = deque(map(int, sys.stdin.readline().split()))

final_list = []
stack_list = []
temp_n = n

Bo = True
target = 1
while len(stu_list) > 0:
    if target == stu_list[0]:
        final_list.append(stu_list.popleft())
        print(final_list)
        print('나감')
        target += 1
    elif target != stu_list[0]:
        print(stack_list)
        print('스택으로')
        if len(stack_list) == 0:
            stack_list.append(stu_list.popleft())
        elif len(stack_list) != 0:
            if stack_list[-1] != target:
                stack_list.append(stu_list.popleft())
            elif stack_list[-1] == target:
                while stack_list[-1] == target:
                    final_list.append(stack_list.pop())
                    print(final_list)
                    print('스택에서 나감')
                    target += 1
        break
            
while len(stack_list) > 0:
    if target == stack_list[-1]:
        final_list.append(stack_list.pop())
        target += 1
    else:
        print('Sad')
        Bo = False
        break

print(stu_list)
print(stack_list)
print(final_list)
if Bo == True:
    print('Nice')
    
    
