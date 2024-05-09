def FibList(n: int) -> str:
    if n <= 1:
        return n
    a, b = 0, 1
    sum = 0
    n = n % 60

    for i in range(2, n + 1):
        sum = sum + b
        a, b = b, (a + b)
    sum += b
    return str(sum)[-1]


n = int(input())
print(FibList(n))
