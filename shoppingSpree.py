def shoppingSpree(prices):
    if len(prices) == 0 or len(prices) == 1:
        return prices
    else:
        ret = [0 for _ in range(len(prices))]
        for i in range(len(prices)):
            j = len(prices)-1
            while j > i:
                dicount = prices[i] - prices[j]
                if dicount >= ret[i]:
                    ret[i] = dicount
                j -= 1
        ret[len(prices) - 1] = prices[len(prices) - 1]
        return ret


################################
# Path: shoppingSpree.py
#################################
# generate test cases
def test_shoppingSpree():
    tests = [[29, 45, 12, 56, 89], [9, 56, 90, 34, 67, 12], [
        34, 78, 45, 80, 60, ], [67, 45, 98, 56, 23], [1, 2, 3, 4, 5]]
    for test in tests:
        print(test, "==> ", shoppingSpree(test))

    prices = [3, 2, 2]
    print("original : ", shoppingSpree(prices))


if __name__ == "__main__":
    test_shoppingSpree()
