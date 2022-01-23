def longest_substring_with_k_distinct(str, key):
    max_len = 0
    for i in range(len(str)-2):
        count = 1
        j = i+1
        while count <= key :
            # print(j)
            if str[i] != str[j]:
                count += 1
            j += 1
        max_len = max(max_len, j-i+1)
    return max_len



if __name__ == '__main__':
    # print(longest_substring_with_k_distinct('cbbebi', 3))
    print(longest_substring_with_k_distinct('araaci', 2))