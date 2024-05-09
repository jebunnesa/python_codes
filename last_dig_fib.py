def FibList(n: int) -> str:
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, (a + b) % 10
    return str(b)[-1]


n = int(input())
print(FibList(n))
