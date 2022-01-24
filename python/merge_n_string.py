def merge_string(string_arr):
    if len(string_arr) == 0:
        return string_arr
    n_string = list(map(lambda x: list(x), string_arr))
    result = ''
    while n_string:
        if len(string_arr[0]) == 0:
            n_string.pop(0)
        current = n_string.pop(0)
        if len(current) != 0:
            result += current.pop(0)
            n_string.append(current)
    return result


print(merge_string(["abcd", "xyz", "pqrs"]))
