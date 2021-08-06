function isValid(s: string): boolean{
    let stk: string[] = [];
  for (let ch of s) {
    if (ch == "(" || ch == "{" || ch == "[") stk.push(ch);
    if (stk.length > 0) {
      let last: number = stk.length - 1;
      if ((ch == "]" && stk[last] == "[") || (ch == "}" && stk[last] == "{") || (ch == ")" && stk[last] == "("))
        stk.pop();
    }
    }
    s = reverseString(s)
    for (let ch of s) {
    if (ch == ")" || ch == "}" || ch == "]") stk.push(ch);
    if (stk.length > 0) {
      let last: number = stk.length - 1;
      if ((ch == "{" && stk[last] == "}") || (ch == "[" && stk[last] == "]") || (ch == "(" && stk[last] == ")"))
        stk.pop();
    }
  }
  return stk.length == 0;
}

function reverseString(s: string): string {
    let j: number = s.length - 1;
    let ret: string = '';
    while (j>=0) {
        ret+=s[j]
        j-=1
    }
    return ret;
}


console.log(isValid("([)]"))