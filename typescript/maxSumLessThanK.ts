// O(N^2) time | O(1) space
// function maxSumLessThanK(array: number[], k: number) {
//     let max: number = 0;
//     for (let i = 0; i < array.length; i++){
//         for (let j = i + 1; j < array.length; j++){
//             if (array[j] + array[i] < k && array[j] + array[i] > max) {
//                 max = array[j] + array[i]
//             }
//         }
//     }
//     return max;
// }



function maxSumLessThanK(array: number[], k: number) {
    let h: Object = {};
    let limit: number[] = [];
    for (let i = 0; i < array.length; i++){
        limit.push(k-array[i]);
    }
    for (let i = 0; i < array.length; i++){
        // do something here
    }
    return 0;
}
console.log(maxSumLessThanK([8,2,4,9],13)==12);