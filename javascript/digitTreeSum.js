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
            return []
        }
        var leftReturnCall = digitTreeSum(tree.left);
        var rightReturnCall = digitTreeSum(tree.right);
        for(var i=0;i<leftReturnCall.length;i++)
            leftReturnCall[i].shift(tree.value);
        for(var i=0;i<rightReturnCall.length;i++)
            rightReturnCall[i].shift(tree.value);
        return [leftReturnCall, rightReturnCall]
    }
    function getValue(array){
        var ret=0;
        for (var i=array.length-1;i>=0;i--)
            ret+=(array.length-1-i)*array[i]
        return ret;
    }
    var result = digitTreeSumHelper(tree)
    var sum=0
    for (var i=0;i<result.length;i++){
        sum+= getValue(result[i])
    }
    return sum;
}