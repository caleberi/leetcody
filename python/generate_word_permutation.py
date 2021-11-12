def word_permutation(s):
    return word_permutation_helper(list(s))
        
def word_permutation_helper(input_list):
    if len(input_list) ==0:
        return ''
    ret = []
    for i in range(len(input_list)):
        base = input_list[i]
        remainder = input_list[:i]+input_list[i+1:]
        out = word_permutation_helper(remainder)
        if isinstance(out,list):
            ret.extend([out[i]+base for i in range(len(out))])
            continue
        else:
            out+=base
        ret.append(out)
    return ret
