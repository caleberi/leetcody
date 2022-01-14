def check_for_sign(s):
    if s[0] == '+' or s[0] != '-':
        return 1
    else:
        return -1


def remove_trailing_whitespace(s):
    return s.strip()


def filter_alpha_string(arr):
    return list(filter(lambda x: not x.isalpha(), arr))


def clean_string(string):
    return''.join(c for c in string if not c.isalpha())


def get_strings(arr):
    return list(map(clean_string, arr))


def convert_string_to_number(s):
    s = remove_trailing_whitespace(s)
    if len(s) == 0:
        return 0
    sign = check_for_sign(s)
    if s[0] == '+' or s[0] == '-':
        s = s[1:]
    # s = get_strings(filter_alpha_string(s.split(' ')))[0]
    s = s.split(' ')[0]
    total = 0
    power = len(s)-1
    idx = 0
    for ch in s:
        if not ch.isnumeric() or ch == '.':
            total = total//(10**(len(s)-idx))
            break
        total += int(ch)*(10**power)
        power -= 1
        idx += 1
    if (total*sign) > 2147483647:
        return 2147483647
    if (total*sign) < -2147483648:
        return -2147483648
    return (total*sign)
