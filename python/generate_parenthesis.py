
from typing import List

OPENING = '('

def is_balanced(parentheses):
    stack = []
    for paren in parentheses:
        if paren == OPENING:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError: 
                return False
    return len(stack) == 0  


def generate_permutation_helper(data):
    if  len(data)==1:
        return [data]
    ret = []
    for i in range(len(data)):
        base = data[i]
        remainder = data[:i]+data[i+1:]
        out = generate_permutation_helper(remainder)
        for o in out:
            ret.append([base]+o)
    return ret

def permute(num) -> List[str]:
    data = ['(']* num + [')']*num
    result = generate_permutation_helper(data)
    y = set(map(lambda x : "".join(x) ,list(filter(lambda x : is_balanced(x),result))))
    return list(y)



if __name__ ==  "__main__":
    print(permute(2))
    # print(permute(5))