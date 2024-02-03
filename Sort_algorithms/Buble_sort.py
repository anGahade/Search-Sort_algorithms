

def bubble_sort(unsorted_list):
    length = len(unsorted_list)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp
                print(unsorted_list)


unsorted_list = [24, 31, 14, 5, 66, 3, 82, 49, 10]
bubble_sort(unsorted_list)
