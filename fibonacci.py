def FibList(n: int, m: int) -> str:
    fib = []
    fib.append(0)
    fib.append(1)

    for i in range(2, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n] % m


n, m = map(int, input().split())
print(FibList(n, m))
