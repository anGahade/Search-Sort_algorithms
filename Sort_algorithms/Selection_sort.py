def selection_sort(arr):
    k = len(arr)
    for i in range(k - 1):
        min_index = i
        for j in range(i + 1, k):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [24, 31, 14, 5, 66, 3, 82, 49, 10]
sorted_arr = selection_sort(arr)
print(sorted_arr)