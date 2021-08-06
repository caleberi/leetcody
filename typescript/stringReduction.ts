function StringReduction(str: string): number{
    return StringReductionHelper(str, 0, str.length).length;
}

function StringReductionHelper(str: string, start: number, end: number): string{
    if (start == end) return str;
    let firstChar = str.charAt(start);
    let nextChar = str.charAt(start + 1);
    let replacement;
    let newString;
    if (nextChar !== firstChar) {
        if (start + 2 < end) {
            replacement = str.charAt(start + 2);
            newString = str.substring(0, start) + replacement + str.substring(start + 2, end);
            str = newString;
        }
    }
    return StringReductionHelper(str,start+1,end)
}

console.log(StringReduction("abcabc"))