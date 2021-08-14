def linear_search(list, target):
    '''
    Returns the index position of the target if found, else returns None
    '''
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

list = range(1, 100 + 1)

print(linear_search(list, 50))
print(linear_search(list, 100))