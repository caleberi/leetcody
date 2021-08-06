# O(N^3) time | O(N) space
def numberOfDistinctSubstringPresent(string):
    ret = []
    for i in range(len(string)):
        s = []
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if isDistinct(substring):
                s.append(substring)
            else:
                break
        ret.extend(s)
    return len(ret)


def isDistinct(string):
    h = {}
    prev = ""
    for i in range(len(string)):
        ch = string[i]
        if ch not in h:
            if prev == "":
                prev = ch
            if prev != "" and prev != ch:
                return False
            h[ch] = True
    return True


# print(numberOfDistinctSubstringPresent("aabbc"))
# print(numberOfDistinctSubstringPresent("aaa"))
# print(numberOfDistinctSubstringPresent("aaallfinvwifn"))
# print(numberOfDistinctSubstringPresent("aaakeosinbaa"))
# print(numberOfDistinctSubstringPresent("gffg"))
# print(numberOfDistinctSubstringPresent("gfg"))


# O(N^2) time | O(N) space
def numberOfDistinctSubstringPresentOptimal(string):
    ret = []
    end = 0
    start = 0
    while start != len(string)-1:
        substring = string[start:end+1]
        unique = isDistinct(substring)
        if unique:
            if start <= end and end == len(string)-1:
                start += 1
                ret.append(substring)
                end = start
                continue
            else:
                ret.append(substring)
                end += 1
                continue
        start += 1
        end = start
    ret.append(string[-1])
    return len(ret)


print(numberOfDistinctSubstringPresentOptimal("aabbc"))
print(numberOfDistinctSubstringPresentOptimal("aaa"))
print(numberOfDistinctSubstringPresentOptimal("aaallfinvwifn"))
print(numberOfDistinctSubstringPresentOptimal("aaakeosinbaa"))
print(numberOfDistinctSubstringPresentOptimal("gffg"))
print(numberOfDistinctSubstringPresentOptimal("gfg"))
print(numberOfDistinctSubstringPresentOptimal("gfg"))
print(numberOfDistinctSubstringPresentOptimal("ABCA"))
print(numberOfDistinctSubstringPresentOptimal("iiiji"))
print(numberOfDistinctSubstringPresentOptimal("aaaba"))
print(numberOfDistinctSubstringPresentOptimal("aaaaaaaaaa"))
