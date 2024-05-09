def major_elem(arr):
    major_val = 0
    dict1 = {}
    for i in arr:
        if i not in dict1:
            dict1[i] = 0
        dict1[i] += 1
    for item in dict1.values():
        major_val = max(major_val, item)
    return 1 if major_val > len(arr) // 2 else 0


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys
    print(major_elem(input_keys))

    # major_val = max(major_val, item)
