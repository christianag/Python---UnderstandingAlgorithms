def buble(list_a):
    sorted = False
    while not sorted: 
        sorted = True
        for i in range(0, len(list_a)-1):
            if list_a[i] > list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                sorted = False
    return list_a

print(buble([2, 9, 1, 4, 0, 7, 6, 3]))
