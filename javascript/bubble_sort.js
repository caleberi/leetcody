function bubble_sort(array,n){
    if(n<=0)
        return
    for (let j = 0; j < array.length-1; j++) {
        if(array[j]>array[j+1]){
            let temp = array[j+1];
            array[j+1] = array[j];
            array[j] = temp;
        }
        
    }
    return bubble_sort(array,n-1);
}

let array = [1,3,8,4,6,2,9,7]
bubble_sort(array,array.length)
console.log(array)