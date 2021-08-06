def valueSort(array):
    sortedArray = sorted(array)
    return reverseArray(sortedArray)


def reverseArray(array):
    i = 0
    j = len(array)-1
    while i <= j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return array


# print(valueSort([1, 1, 2, 3]))
# print(valueSort([5, 2, 4, 4, 9, 2, 2]))


assert(valueSort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2])
assert(valueSort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2])
