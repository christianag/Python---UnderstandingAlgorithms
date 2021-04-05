def binary_search(sequence, item):
    start_index = 0
    end_index = len(sequence) - 1

    while start_index != end_index:
        midpoint = start_index + (end_index - start_index) // 2
        mid_value = sequence[midpoint]

        if mid_value == item:
            return midpoint
        elif mid_value < item:
            start_index = midpoint+1
        else:
            end_index = midpoint-1

    return None

list_a = [9, 3, 2, 7, 6, 1, 5, 4, 0]
target = 2
print(binary_search(list_a, target))