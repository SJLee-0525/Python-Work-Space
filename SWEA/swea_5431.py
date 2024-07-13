t = int(input())

for tt in range(t):
    student, submit = map(int, input().split())
    student_list = list(range(1, student + 1))
    submit_list = list(map(int, input().split()))

    for s in submit_list:
        student_list.remove(s)
    
    print('#', end = '')
    print(tt + 1, *student_list)
