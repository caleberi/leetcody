function sumUnqiueElements(arr){
    let kdict = {};
    let vdict = {}
    for(var a in arr){
        if (kdict[a]){
            kdict[a]++;
            vdict[kdict[a]].push(a)
        }else{
            kdict[a]=1;
            vdict[kdict[a]]=[a];
        }
    }

    return vdict[1];
}

console.log(sumUnqiueElements([1, 3,3,5,2, 5, 2]))