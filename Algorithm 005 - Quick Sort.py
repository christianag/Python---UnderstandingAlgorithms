def quick_sort(list_a):
    length = len(list_a)

    if length <= 1:
        return list_a
    else: 
        pivot = list_a.pop()

    items_lower = []
    items_greater = []

    for item in list_a:
        if pivot > item:
            items_lower.append(item)
        else:
            items_greater.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([9, 3, 2, 7, 6, 1, 5, 4, 0]))