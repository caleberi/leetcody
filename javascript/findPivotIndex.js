var pivotIndex = function (nums = []) {
    if (nums.length==1) 
        return 0;
    let leftSum = 0; 
    let pivot = 0;
    let rightSum = 0;

    for(let i = nums.length-1; i>0;i--)
        rightSum += nums[i];

    while(pivot < nums.length-1){
        if(leftSum == rightSum)
            return pivot;
        leftSum += nums[pivot];
        pivot++;
        rightSum -= nums[pivot];
    }
    if(leftSum == rightSum)
        return pivot;
    return -1;
};

console.log(pivotIndex([1, 7, 3, 6, 5, 6]))
console.log(pivotIndex([1, 2, 3]))
console.log(pivotIndex([2, 1, -1]))
console.log(pivotIndex([-1,-1,0,0,-1,-1]));