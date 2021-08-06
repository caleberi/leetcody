
//  * Definition for a binary tree node.
 class TreeNode {
     val: number
     left: TreeNode | null
     right: TreeNode | null
     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.left = (left===undefined ? null : left)
         this.right = (right===undefined ? null : right)
     }
  }
 

function sumNumbers(root: TreeNode | null): number {
    return sumNumbersHelper(root)[0];
};

function isLeaf(node:TreeNode|null):boolean{
    return node.left==null&& node.right==null;
}

function sumNumbersHelper(root: TreeNode):[number,number]{
    if(isLeaf(root)){
        return [root.val,0]
    }
    
    let leftResult = sumNumbersHelper(root.left);
    let leftDigit:number= leftResult[0]*Math.pow(10,leftResult[1]); // 5
    let rightResult = sumNumbersHelper(root.right);
    let rightDigit:number= rightResult[0]*Math.pow(10,rightResult[1]); //1
    let currentLeftDigitPlusNode:number = root.val*Math.pow(10,leftResult[1]+1)+leftDigit; // 95
    let currentRightDigitPlusNode:number = root.val*Math.pow(10,rightResult[1]+1)+rightDigit; //91
    let total:number = currentLeftDigitPlusNode+currentRightDigitPlusNode; // 95+91
    return [total,leftResult[1]+rightResult[1]+2]
}