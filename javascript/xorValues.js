// Given two integers, N and start, return the result of applying 
// the XOR operation to N values beginning from start.
// Note: Each value that is calculated should be formed as 
// follows: start + 2 * i (where i is the ith value you're calculating).

// Ex: Given the following N and start…

// N = 3, start = 0, return 6 (0 ^ 2 ^ 4 = 6).
// Ex: Given the following N and start…

// N = 5, start = 3, return 3.

function xorValues(n,start){
    let sum=0;
    let i=0;
    for(i = 0; i<n; i++){
        sum=sum^(start+2*i);
    }
    return sum;
}
