def gcd_of_a_b(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


a, b = map(int, input().split())
print(gcd_of_a_b(a, b))
