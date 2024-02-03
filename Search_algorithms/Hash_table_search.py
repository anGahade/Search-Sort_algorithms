def hash_table_search(table, key):
    for i in range(len(table)):
        if table[i] == key:
            return i
    return -1


table = [2, 5, 7, 10, 12, 15, 20, 25, 30]
key = 2
result = hash_table_search(table, key)
if result != -1:
    print(f"Елемент {key} знайдено на позиції {result}.")
else:
    print(f"Елемент {key} не знайдено в масиві.")
