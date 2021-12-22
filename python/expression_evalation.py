# def solve(s):
#     if "()" in s:
#         return "invalid"
#     def result(op1, op2, opr):
#         x = int(op1)
#         y = int(op2)
#         if opr == "+":
#             return int(x+y)
#         elif opr == "*":
#             return int(x*y)
#         elif opr == "-":
#             return int(x-y)
#         elif opr == "/":
#             return int(x/y)

#     opStk = []
#     oprStk = []
#     curr_num = []
#     for i in range(len(s)):
#         ch = s[i]
#         if ch in "+-/*":
#             if len(oprStk)>=2 and len(opStk)==0:
#                 return "invalid"
#             if len(curr_num) > 0:
#                 opStk.append(int("".join(curr_num)))
#                 curr_num =[]
#             if len(opStk) > 2:
#                 op1 = opStk.pop()
#                 op2 = opStk.pop()
#                 opr = oprStk.pop()
#                 opStk.append(result(op1, op2, opr))
#                 oprStk.append(ch)
#                 continue
#             oprStk.append(ch)
#         elif ch in "()":
#             continue
#         elif ch.isdigit():
#             curr_num.append(ch)
#     if len(curr_num):
#         opStk.append(int("".join(curr_num)))
#         curr_num =[]
#     while len(oprStk)>0:
#         op1 = opStk.pop()
#         op2 = opStk.pop()
#         opr = oprStk.pop()
#         opStk.append(result(op1, op2, opr))
#     if len(oprStk)>1 or len(opStk)>1:
#         return "invalid"
#     if len(opStk)==0:
#         return "invalid"
#     return opStk[0]  if opStk[0] >= 0 else "invalid"


# print(solve("(1+2)*3"))


def result(op1, op2, opr):
    x = int(op1)
    y = int(op2)
    if opr == "+":
        return int(x+y)
    elif opr == "*":
        return int(x*y)
    elif opr == "-":
        return int(x-y)
    elif opr == "/":
        return int(x/y)

def mod(a, m):
    return (a%m + m) % m

def solve(s):
    if "()" == s or s.startswith("()") :
        return "invalid"
    
    operators = []
    operands = []
    num = []
    
    for i in range(len(s)):
        ch = s[i]
        if ch in "+-/*":
            if len(operators)>=2 and len(operands)==0:
                return "invalid"
            if len(num) > 0:
                operands.append(int("".join(num)))
                num =[]
            if len(operands) > 2:
                op1 = operands.pop()
                op2 = operands.pop()
                opr = operators.pop()
                operands.append(result(op1, op2, opr))
                continue
            operators.append(ch)
        elif ch in "(":
            continue
        elif ch.isdigit():
            num.append(ch)
    if len(num):
        operands.append(int("".join(num)))
        curr_num =[]
    while len(operators)>0:
        op1 = operands.pop()
        op2 = operands.pop()
        opr = operators.pop()
        operators.append(result(op1, op2, opr))
    if len(operators)>1 or len(operands)>1:
        return "invalid"
    if len(operands)==0:
        return "invalid"
    return mod(operands[0],1000000007) if operands[0] >= 0 else "invalid"
    
    