from typing import List


def solution(n: int, arr: List) -> int:
    arr.sort()
    return arr[-1] * arr[-2]


n = int(input())
arr = list(map(int, input().split()))
print(solution(n, arr))
