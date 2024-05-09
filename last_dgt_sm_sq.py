def FibList(n: int) -> str:
    if n <= 1:
        return str(n)
    a, b = 0, 1
    sum = 1
    # n = n % 30

    for i in range(2, n + 1):
        a, b = b, (a + b)
        sum = sum + b * b
    return str(sum)[-1]


n = int(input())
print(FibList(n))
