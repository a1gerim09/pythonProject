def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def binary_search(lst, element):
    first = 0
    last = len(lst)-1
    while first <= last:
        middle = (first + last) // 2
        if lst[middle] == element:
            return middle
        elif lst[middle] < element:
            first = middle + 1
        else:
            last = middle - 1
    return -1


lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = bubble_sort(lst)
print(sorted_lst)
index = binary_search(sorted_lst, 64)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in list")


