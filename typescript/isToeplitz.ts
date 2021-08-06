// type Matrix = Array<Array<number>>;

// function checkIfDiagonalDistinct(diagonal: Array<number>): boolean {
//     let set: Set<number> = new Set<number>(diagonal);
//     return set.size==1?true:false;
// };

// enum Direction {
//     moveLeft=1,
//     moveDown
// };

// function isOutBound(matrix:Matrix,i:number,j:number):boolean {
//     return (i<0||i>matrix.length-1|| j<0 ||j>matrix[i].length-1)
// };


// function isToeplitz(matrix: Matrix): boolean{ 
//     let i: number = 0;
//     while (i < matrix.length) {
//         let x: number = 0;
//         let y: number = 0;
//         let xc: number = x;
//         let yc: number = y;
//         let current: number[]=[];
//         while(xc<=matrix.length){
//             if(xc==matrix.length){
//                 xc=0;
//                 yc=y+1;
//                 continue;
//             }
//             current.push(matrix[xc][yc]);
//             xc++;
//             yc++;
//         }
//         i++;
//     }
//     return true;
// }


type Matrix = Array<Array<number>>;

function checkIfDiagonalDistinct(diagonal: Array<number>): boolean {
    let set: Set<number> = new Set<number>(diagonal);
    return set.size==1?true:false;
};

function isOutBound(matrix:Matrix,i:number,j:number):boolean {
    return (i<0||i>matrix.length-1|| j<0 ||j>matrix[i].length-1)
};


function isToeplitz(matrix: Matrix): boolean{ 
    let i: number = 0;
    while (i < matrix.length) {
        let x: number = i;
        let y: number = 0;
        let xc: number = x;
        let yc: number = y;
        let current: number[]=[];
        while(xc<=matrix.length){
            if(xc==matrix.length){
                if (!checkIfDiagonalDistinct(current)) return false;
                current=[]
                xc=0;
                yc=y+1;
                continue;
            }
            if(isOutBound(matrix,xc,yc)){
                if (!checkIfDiagonalDistinct(current)) return false;
                current=[]
                xc=0;
                yc=y+1;
                continue;
            }
            current.push(matrix[xc][yc]);
            xc++;
            yc++;
        }
        console.log(current);
        i++;
    }
    return true;
}

console.log(isToeplitz(
    [
        [1,2,3],
        [4,1,2],
        [5,4,1],
    ]
))
