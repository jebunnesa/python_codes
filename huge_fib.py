def FibList(n: int, m: int) -> str:
    if n <= 1:
        return n
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, (a + b) % (m*10)
    return b % m


n, m = map(int, input().split())
print(FibList(n, m))
