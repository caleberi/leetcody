
def uniqueLetterString(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += countUniqueChars(s[i:j+1])
    return count % 10000000007


def countUniqueChars(string):
    seenbutDeleted = set()
    history = {}
    for s in string:
        if s not in history and s in seenbutDeleted:
            continue
        elif s not in history and s not in seenbutDeleted:
            history[s] = len(s)
        else:
            seenbutDeleted.add(s)
            del history[s]
    return len(history.items())


print(uniqueLetterString("LEETCODE"))
