class Solution:
    def solve(self, s):
        def getResult(op1, op2, opr):
            x = int(op1)
            y = int(op2)
            if opr == "+":
                return str(x+y)
            elif opr == "*":
                return str(x*y)
            elif opr == "-":
                return str(x-y)
            elif opr == "/":
                return str(x/y)

        opStk = []
        oprStk = []
        for i in range(len(s)+1):
            if i == len(s):
                break
            ch = s[i]
            if ch in "+-/*":
                if len(opStk) > 2:
                    op1 = opStk.pop()
                    op2 = opStk.pop()
                    opr = oprStk.pop()
                    opStk.append(getResult(op1, op2, opr))
                    continue
                oprStk.append(ch)
            elif ch in "()":
                continue
            else:
                opStk.append(ch)
        print(opStk)
        print(oprStk)
        return opStk[0]


s = "1+2*4/6"
ans = 2
