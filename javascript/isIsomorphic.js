function arrayEquals(a, b) {
    return Array.isArray(a) &&
        Array.isArray(b) &&
        a.length === b.length &&
        a.every((val, index) => val === b[index]);
}

var isIsomorphic = function(s, t) {
    let sh = {} ,th = {};
    if (s.length!=t.length)
        return false;
    for (let idx = 0; idx < s.length; idx++) {
        const skey = s[idx];
        const tkey = t[idx];
        if (!(skey in sh )||!(tkey in th)){
            sh[skey] = 1;
            th[tkey] = 1;
            continue;
        }
        sh[skey] ++;
        th[tkey] ++;
    }
    return arrayEquals(Object.values(sh),Object.values(th));
};

console.log(isIsomorphic("egg","add"));