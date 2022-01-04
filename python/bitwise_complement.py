def bitwiseComplement(n):
    if n == 0:
        return 1
    bits = []
    while n:
        r = n % 2
        bits.append(r)
        n = n//2
    rev_bits = [0 if bit == 1 else 1 for bit in bits]
    number = 0
    i = 0
    for r in rev_bits:
        number += r*(2**i)
        i += 1
    return number
