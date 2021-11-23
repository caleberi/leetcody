def recursive_linear_search(arr,target,i=0):
    if len(arr)==0:
        return -1
    if i == len(arr):
        return -1
    if arr[i]==target:
        return i
    return recursive_linear_search(arr,target,i+1)


print(recursive_linear_search([3,2,5,6,7,8,1,9],9))