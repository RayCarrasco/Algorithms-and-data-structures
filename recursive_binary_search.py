def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        print(midpoint)

        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1:], target)
        elif list[midpoint] > target:
            return recursive_binary_search(list[:midpoint], target)

list = range(1, 101)
print(recursive_binary_search(list, 101))