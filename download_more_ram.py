def download_more_ram(n, current_ram_size, software_ram, gain_ram):
    flag = []
    for k in range(n):
        flag.append(0)
    for j in range(n):
        for i in range(n):
            if software_ram[i] <= current_ram_size and flag[i] != 1:
                current_ram_size += gain_ram[i]
                flag[i] = 1
    print(current_ram_size)


def main():
    t = int(input())
    for t in range(t):
        arr = list(map(int, input().split()))[:2]
        n = arr[0]
        current_ram_size = arr[1]
        software_ram = list(map(int, input().split(' ')[:n]))
        gain_ram = list(map(int, input().split(' ')[:n]))
        download_more_ram(n, current_ram_size, software_ram, gain_ram)


main()