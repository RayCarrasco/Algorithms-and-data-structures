def binary_search(list, target):
    ''''
    
    '''
    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        midpoint = (lower + upper) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            lower = midpoint + 1
        elif list[midpoint] > target:
            upper = midpoint - 1
    return None


list = range(1, 100 + 1)
print(binary_search(list, 80))
