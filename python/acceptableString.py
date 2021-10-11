def acceptableString(string):
    if len(string) == 0:
        return ""
    stk = [string[0]]
    for idx in range(1, len(string)):
        ch = string[idx]
        if len(stk) and ch.islower() and stk[-1].isupper():
            _ = stk.pop()
        elif len(stk) and ch.isupper() and stk[-1].islower():
            _ = stk.pop()
        else:
            stk.append(ch)
    return "".join(stk)


print(acceptableString("aaBbc"))
print(acceptableString("Aabb"))
print(acceptableString("AabBcC"))
print(acceptableString("kinangYRUnkiOp"))
print(acceptableString("aaBbcyeS"))
print(acceptableString("aaBbclinfO"))
