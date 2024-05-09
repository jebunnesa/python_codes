input_array = [100, 9, 1, 5, 55, 6, 19, 1001]

n = len(input_array)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if input_array[min_index] > input_array[j]:
            min_index = j
    input_array[i],  input_array[min_index] = input_array[min_index],  input_array[i]
print(input_array)
