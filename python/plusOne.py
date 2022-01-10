def plusOne(digits):
    power = len(digits)-1
    total = 1
    for i in range(len(digits)):
        total += digits[i]*(10**power)
        power -= 1
    ret = []
    while total:
        r = total % 10
        total = total//10
        ret.append(r)
    ret.reverse()
    return ret


print(plusOne([1, 2, 3]))
