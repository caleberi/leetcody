def canPlaceFlowers(flowerbed, n):
    for i in range(0, len(flowerbed)):
        if can_be_fixed(flowerbed, i):
            flowerbed[i] = 1
            if n == 0:
                break
            n -= 1
    return n == 0


def can_be_fixed(arr, i):
    if i == 0:
        if i+1 >= len(arr) and arr[i] == 0:
            return True
        return arr[i] == 0 and arr[i+1] == 0
    elif i == len(arr)-1:
        return arr[i] == 0 and arr[i-1] == 0
    elif i > 0 and i < len(arr)-1:
        return arr[i-1] == 0 and arr[i] == 0 and arr[i+1] == 0
    return False


print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
print(canPlaceFlowers([0, 0, 1, 0, 0], 1))
