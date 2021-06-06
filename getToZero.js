/**
 * Given a non-negative integer, num, return the number of operations it takes to reduce it to zero. If num is even, divide it by two. If num is odd, 
 * subtract one from it. Continue this process until num is zero.
 */

function numberOperations(number,count=0){
    if (number==0) return count;
    else if(number%2==0) return numberOperations(number/2,count+1);
    else if(number%2==1) return numberOperations(number-1,count+1);
}

console.log(numberOperations(5)); 
console.log(numberOperations(16)); 