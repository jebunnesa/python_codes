def FibList(m:int, n: int) -> str:
    if n <= 2:
        return n
    a, b = 0, 1
    sum = 0
    for i in range(2, n + 1):
        a, b = b, (a + b)
        if i >= m:
            sum = sum + b
    return str(sum)[-1]


n, m = map(int, input().split())
print(FibList(n, m))
