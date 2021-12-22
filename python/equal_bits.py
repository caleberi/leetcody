"""
Given an integer array, bits, that represents 
a binary sequence (i.e. it only contains zeroes and ones),
return the length of the longest contiguous sequence of bits that contains the same number of zeroes and ones.

Ex: Given the following bits ...
bits = [1, 0, 1, 1, 0, 0], return 6 (the entire sequence has the 3 zeroes and 3 ones).
Ex: Given the following bits ...

bits = [1, 1], return 0.
"""
def equal_bits(bits_sequence):
    if len(bits_sequence)<=1:
        return 0
    if len(bits_sequence)==2:
        if ((bits_sequence[0] == 1 and bits_sequence[1]==0) or
                 (bits_sequence[1]==0 and bits_sequence[0]==1)):
            return 2
        return 0
    max_len  = 0
    i=0
    while i<len(bits_sequence):
        ones = 0
        zeros= 0
        j = i 
        while j  < len(bits_sequence):
            if bits_sequence[j]==0:
                zeros+=1
            if bits_sequence[j]==1:
                ones+=1
            j+=1
        if zeros==ones:
            max_len = max(max_len,zeros+ones)
        i+=1
    
    return max_len

if __name__  == "___main__":
    print(equal_bits([1, 0, 1, 1, 0, 0]))
