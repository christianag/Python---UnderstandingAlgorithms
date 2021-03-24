def selection_sort(list_a):
    for i in range(0, len(list_a)- 1):
        min_value = i
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a

print(selection_sort([9, 2, 4, 6, 1, 0, 5]))