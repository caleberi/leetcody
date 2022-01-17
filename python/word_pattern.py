

def wordPattern(pattern, s):
    pattern_arr = list(pattern)
    string_arr = s.split(' ')
    if len(pattern_arr) != len(string_arr):
        return False
    table = create_translation_table(string_arr, pattern)
    print(table)
    for idx, symbol in enumerate(pattern):
        print(symbol)
        if symbol in table:
            pattern_arr[idx] = table[symbol]
        else:
            return False
    return ' '.join(pattern_arr) == s


def create_translation_table(string_arr, pattern):
    table_a = {}
    table_b = {}
    for idx, ch in enumerate(string_arr):
        if pattern[idx] in table_a or string_arr[idx] in table_b:
            continue
        table_a[pattern[idx]] = ch
        table_b[ch] = pattern[idx]

    return table_a


print(wordPattern('abba', 'dog cat cat dog'))
print(wordPattern('abba', "dog cat cat fish"))
print(wordPattern('aaaa', "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))
