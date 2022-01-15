if __name__ == '__main__':
    t = int(input())
    n, m, r, c =map(int, input().split())
    arr = []
    for i in range(n):
        arr.append([])
        arr[i] = [map(input().split() for j in range(m))]
    print(arr)

