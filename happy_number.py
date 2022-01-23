def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))
        if slow == fast:
            break
    return slow == 1


def square_sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit*digit
        num //= 10
    return sum


if __name__ == '__main__':
    print(find_happy_number(12))
    print(find_happy_number(13))