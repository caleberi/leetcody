# 54 / 56 test cases passed.
# Status: Runtime Error
# Time limit exceeded
# 0(N^2)
def oneSubstrings(string):
    if string == "" or len(string) == 0:
        return 0
    if len(string) == 1 and string == "1":
        return 1
    if len(string) == 1 and string == "0":
        return 0
    count = 0
    for i in range(len(string)):
        r = ""
        for j in range(i, len(string)):
            if "0" == string[j]:
                break
            r += string[j]
            count += 1
    return count


# generate test cases for oneSubstrings
def test_oneSubstrings():
    print("\nTesting oneSubstrings1 ... ", end="")
    assert(oneSubstrings("") == 0)
    assert(oneSubstrings("1") == 1)
    assert(oneSubstrings("0") == 0)
    assert(oneSubstrings("101") == 2)
    assert(oneSubstrings("10101") == 3)
    assert(oneSubstrings("101010") == 3)
    assert(oneSubstrings("1010101") == 4)
    assert(oneSubstrings("10101010") == 4)
    assert(oneSubstrings("101010101") == 5)
    assert(oneSubstrings("1010101010") == 5)
    assert(oneSubstrings("10101010101") == 6)
    assert(oneSubstrings("101010101010") == 6)
    assert(oneSubstrings("1010101010101") == 7)
    print("Passed!")
    print("\nTesting oneSubstrings2 ... ", end="")
    assert(oneSubstrings("1011") == 4)
    assert(oneSubstrings("101101") == 5)
    assert(oneSubstrings("000") == 0)
    print("Passed!")


if __name__ == "__main__":
    test_oneSubstrings()
    # print(oneSubstrings(input()))

# print("yes")
