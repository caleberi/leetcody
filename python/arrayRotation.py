def array_rotation(arr):
    i =len(arr)-1
    while i > -1:
        if arr[i-1]<arr[i]:
            i-=1
            continue
        break
    print( arr[i])
    return True if i>=0 and arr[i-2]<arr[len(arr)-1] else False
        



print(array_rotation([4, 5, 1, 2, 3]))
print(array_rotation([4, 5, 1, 2, 3, 6]))