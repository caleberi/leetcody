# You are given an integer array that represents the prices of items in a store.
# The ith price is given by prices[i]; however, the store is running a special
# discount.
# By buying the ith item, you receive a discount of prices[j] where prices[j] 
# is less than or equal to prices[i] and j > i.
# If no such prices[j] exists, you pay for price for the ith item.
# Given these prices, return an array that represents the amount you’ll 
# pay for each respective item considering the special discount.

# Ex: Given the following prices…
# prices = [3, 2, 2], return [1, 0, 2].
# For prices[0] you pay 3 - 1 = 1 dollars.
# For prices[1] you pay 2 - 2 = 0 dollars.
# For prices[2] you pay 2 - 2 = 0 dollars.

############################################################################################
# Path: shoppingSpree.py
#################################
# generate test cases
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
