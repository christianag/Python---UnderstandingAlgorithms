def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        value = list_a[i]
        while list_a[i-1] > value and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1
    return list_a

print(insertion_sort([3, 4, 1, 2, 7, 9]))

