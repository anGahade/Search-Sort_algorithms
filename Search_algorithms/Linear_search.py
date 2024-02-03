def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [2, 5, 7, 10, 12, 15, 20, 25, 30]
target = 87
result = linear_search(arr, target)
if result != -1:
    print(f"Елемент {target} знайдено на позиції {result}.")
else:
    print(f"Елемент {target} не знайдено в масиві.")