def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i
        while j > 0 and arr[j - 1] > value:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value
    return arr


arr = [24, 31, 14, 5, -66, 3, 82, 49, 10]
sorted_arr = insertion_sort(arr)
print(f"Sorted array: {sorted_arr}")
