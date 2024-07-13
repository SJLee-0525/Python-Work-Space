import sys

l = [0] * 10001
n = int(sys.stdin.readline())

for _ in range(n):
    l[int(sys.stdin.readline())] += 1

for i in range(10001):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)


# https://kevinitcoding.tistory.com/entry/%EB%B0%B1%EC%A4%80Python-10989%EB%B2%88-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%EB%AC%B8%EC%A0%9C