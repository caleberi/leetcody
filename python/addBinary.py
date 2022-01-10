def to_decimal(str):
    total = 0
    length = len(str)
    power = 0
    for i in range(length):
        idx = length-1-i
        total += int(str[idx]) * (2**power)
        power += 1
    return total


def to_binary(num):
    if num == 0:
        return '0'
    bit = []
    while num:
        r = num % 2
        num = num//2
        bit.append(f'{r}')
    bit.reverse()
    return ''.join(bit)


def addBinary(a, b):
    a_decimal = to_decimal(a)
    b_decimal = to_decimal(b)
    sum_decimal = a_decimal+b_decimal
    return to_binary(sum_decimal)
