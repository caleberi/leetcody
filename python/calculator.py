
def calculate(s:str):
    def get_result(op1, op2, opr):
        x = op1
        y = op2
        match opr:
            case "+":
                return x+y
            case "*":
                return x*y
            case "-":
                return x-y
            case "/":
                return x/y

    ret = []
    s = s.replace(" ", "")
    n = 0
    p = 0

    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            n += int(ch) * (10**p)
            p += 1 
        elif ch in "+/*-":
            if n >= 0:
                if len(ret) >=2:
                    opr = ret.pop()
                    opr1= ret.pop() 
                    ret.append(get_result(opr1,n,opr))
                
        # elif ch in "+/*-":
        #     if n != 0:
        #         print(ret)
        #         while len(ret) or ret[-1] != '(':
        #             if len(ret) >=2:
        #                 opr = ret.pop()
        #                 opr1= ret.pop() 
        #                 ret.append(get_result(opr1,n,opr))
        #                 print(ret)
        #             elif len(ret) < 2:
        #                 opr = ret.pop()
        #                 if opr == '-':
        #                     n = -n
        #                 ret.append(n)
        #     p = 0
        #     n = 0
        #     ret.append(n)
        # elif ch in '()':
        #     ret.append(ch)
    return ret




print(calculate("(1+2+3+(45+56)-8)"))

