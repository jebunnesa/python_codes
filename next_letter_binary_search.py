def search_next_letter(str, ch):
    n = len(str)
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end - start) // 2
        if str[mid] > ch:
            end = mid - 1
        else:
            start = mid+1
    return str[start%n]




def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()