def minimum_abs_difference(arr):
    result = []
    differences = []
    arr.sort()
    for i in range(1,len(arr)):
        d = bts_search(arr,0,i)
        result.append([d,arr[i]])
        differences.append(abs(d-arr[i]))
    
    return list(sort_result_with_difference(result,differences))

def sort_result_with_difference(result,differences):
    mn_diff = min(differences)
    return filter(lambda x : abs(x[0]-x[1])==mn_diff,result)
    
def bts_search(array,start,end):
    i=start
    j=end
    while(i<j):
        mid = int(i+(j-i)/2)
        if mid+1 >= end:
            return array[mid]
        elif mid+1 < end and array[mid] < array[mid+1]: 
            i = mid+1
        else:
            j = mid-1
    return -1