def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [2, 5, 7, 10, 12, 15, 20, 25, 30]
target = 2
result = binary_search(arr, target)
if result != -1:
    print(f"Елемент {target} знайдено на позиції {result}.")
else:
    print(f"Елемент {target} не знайдено в масиві.")