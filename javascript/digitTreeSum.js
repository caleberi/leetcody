class Tree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function digitTreeSum(tree){
    function digitTreeSumHelper(tree){
        if (tree==null){
            return [0,1];
        }
        if (tree.left==null&& tree.right ==null){
            return [tree.value,1]
        }

        var [lvalue,ldecimal] = digitTreeSum(tree.left);
        var [rvalue,rdecimal] = digitTreeSum(tree.right);
        var total = (lvalue*ldecimal)+(rdecimal*rdecimal);
        return [total, Math.max(ldecimal,rdecimal)*10]
    }
    
    var result = digitTreeSumHelper(tree)
    var sum=0
    for (var i=0;i<result.length;i++){
        sum+= getValue(result[i])
    }
    return sum;
}


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
 var sumNumbers = function(root) {
    function digitTreeSumHelper(tree){
        if (tree==null){
            return [0,1];
        }
        if (tree.left==null&& tree.right ==null){
            return [tree.value,1]
        }

        var [lvalue,ldecimal] = digitTreeSum(tree.left);
        var [rvalue,rdecimal] = digitTreeSum(tree.right);
        var total = (lvalue*ldecimal)+(rdecimal*rdecimal);
        return [total, Math.max(ldecimal,rdecimal)*10]
    }
    return digitTreeSumHelper(root);
};