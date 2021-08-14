def merge_sort(list: list) -> list:
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sor the sublist created in previuus step
    Combine: Merge the sorted sublists created in prviou step

    Takes O (n log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list: list) -> tuple:
    """
    Divide the unsorted list at midpoint into sublist
    Returns two sublist  left and right

    Takes overall O(log n) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left: list, right: list) -> list:
    """
    Merges two list (arrays), sorting them in the process
    Returns a new merge list

    Runs in overall O(n) time.
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def veryfy_sorted(list: list) -> bool:
    """
    
    """
    n = len(list)

    if n <= 1:
        return True
    
    return list[0] < list[1] and veryfy_sorted(list[1:])

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(veryfy_sorted(alist))
print(veryfy_sorted(l))