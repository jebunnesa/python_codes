def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a: int, b: int) -> int:
    gcd_val = gcd(a, b)
    res = int((a*b)/gcd_val)
    return res


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
