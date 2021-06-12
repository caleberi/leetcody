function subtractProductAndSum(n: number) {
    let product: number = 1;
    let sum: number = 0;
    let tmp:number = n;
    while (tmp != 0) {
        let remainder: number = tmp % 10;
        product*=remainder;
        let quotient: number = Math.floor(tmp / 10);
        tmp = quotient;
    }
    tmp= n;
    while (tmp != 0) {
        let remainder: number = tmp % 10;
        sum+=remainder;
        let quotient: number = Math.floor(tmp / 10);
        tmp = quotient;
    }
    return product - sum;
}

console.log(subtractProductAndSum(321))
console.log(subtractProductAndSum(56))
console.log(subtractProductAndSum(234))
console.log(subtractProductAndSum(4421))