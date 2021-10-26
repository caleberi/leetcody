function fib(num){
    if (num<=0)
        throw {message:"value cannot negative or zero",code:10011};
    if(num==1||num==2)
        return 1;
    return fib(num-1) + fib(num-2);
}


console.log(fib(5));
console.log(fib(0))