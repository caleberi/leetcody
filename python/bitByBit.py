# Given an array of integers, nums, return an array that contains nums sorted in ascending order according to their number of one bits.
# Note: If two values have the same number of one bits, they should be sorted in ascending order.
# Ex: Given the following nums…
#     nums = [5, 2, 8], return [2, 8, 5] (2 has 1 one bit, 8 has 1 one bit, 5 has 2 one bits).
# Ex: Given the following nums…
#     nums = [4, 5, 5, 1, 3, 9], return [1, 4, 3, 5, 5, 9].

def bitsByBit(numbers):
    bitCount = getBitCountArray(numbers)
    numWithBitCount = zip(numbers, bitCount)
    lnumWithBitCount = list(numWithBitCount)
    sortByBit = mergeSort(lnumWithBitCount)
    result = extractFromlnumWithBitCnt(sortByBit)
    return result


def mergeSort(number):
    if len(number) == 1:
        return number
    mid = len(number)//2
    leftHalf = number[:mid]
    rightHalf = number[mid:]
    return merge(mergeSort(leftHalf), mergeSort(rightHalf))


def merge(leftHalf, rightHalf):
    i = j = k = 0
    tarr = [None] * (len(leftHalf)+len(rightHalf))
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i][1] < rightHalf[j][1]:
            tarr[k] = leftHalf[i]
            i += 1
        elif leftHalf[i][1] == rightHalf[j][1]:
            if leftHalf[i][0] < rightHalf[j][0]:
                tarr[k] = leftHalf[i]
                i += 1
            else:
                tarr[k] = rightHalf[j]
                j += 1
        else:
            tarr[k] = rightHalf[j]
            j += 1
        k += 1
    while j < len(rightHalf):
        tarr[k] = rightHalf[j]
        j += 1
        k += 1
    while i < len(leftHalf):
        tarr[k] = leftHalf[i]
        i += 1
        k += 1
    return tarr


def countOneInBit(n):
    count = 0
    while n != 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count


def getBitCountArray(numbers):
    ret = []
    for i in range(len(numbers)):
        bitCnt = countOneInBit(numbers[i])
        ret.append(bitCnt)
    return ret


def extractFromlnumWithBitCnt(lnumWithBitCount):
    result = []
    for i in range(len(lnumWithBitCount)):
        result.append(lnumWithBitCount[i][0])
    return result


print(bitsByBit([5, 2, 8, 9, 3, 75, 23, 2, 46]))
print(bitsByBit([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(bitsByBit([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(bitsByBit([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(bitsByBit([4, 5, 5, 1, 3, 9]))
