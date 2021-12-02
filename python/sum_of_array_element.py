def sum_of_element(arr,idx):
    if idx==0:
        return arr[idx]
    arr[idx] = arr[idx]+ sum_of_element(arr,idx-1) 
    return arr[idx]


def update_arr_with_sum(array):
    sum_of_element(array,len(array)-1)
    return array


if __name__ == "__main__":
    print(update_arr_with_sum([1,2,3,4,5,6]))
