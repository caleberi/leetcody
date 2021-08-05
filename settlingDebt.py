# You and your friends went on a vacation. During this vacation you and
# your friends paid for one another for various things like food and entertainment.
# For example, Kevin might have paid $20 for Alex’s food. Now that the vacation is over,
# it’s time to settle your debts. Given a list of transactions representing the payments between people ([0, 1, 20] representing person 0 paid for person 1 $10), return the minimum number of transactions to settle all debts.

# Ex: Given the following transactions…

# transactions = [[0, 1, 20]], return 1 (person 1 must pay person 0 $10 back).
# Ex: Given the following transactions…

# transactions = [[0, 1, 5], [0, 2, 10], [2, 1, 15]], return 2.

class Mapped:
    def __init__(self):
        self.mapped = {}
        self.count = 0

    def add(self, key, value):
        if key in self.mapped:
            self.mapped[key].add(value)
        self.mapped[key] = {value}

    def contains(self, key, value):
        if key not in self.mapped:
            return key in self.mapped and value in self.mapped[key]
        return True

    def print(self):
        for key, value in self.mapped.items():
            print(key, value, sep=" --> ", end="\n")

# WRONG APPROACH !!!

def settlingDebts(transactions):
    m = Mapped()
    return settlingDebtsHelper(transactions, m)


def settlingDebtsHelper(transactions, m: Mapped):
    if len(transactions) == 0:
        return 0
    if transactions[0][0] != transactions[0][1] and not m.contains(transactions[0][0], transactions[0][1]):
        m.add(transactions[0][0], transactions[0][1])
        return 1 + settlingDebtsHelper(transactions[1:], m)
    return 0+settlingDebtsHelper(transactions[1:], m)


# print(settlingDebts([[0, 1, 20], [0, 2, 10], [2, 1, 15]]))

# generate test for settlingDebt


def test_settlingDebt():
    assert settlingDebts([[0, 1, 10], [1, 2, 10]]) == 2
    assert settlingDebts([[0, 1, 20], [0, 1, 10], [0, 1, 15]]) == 1
    assert settlingDebts([[0, 1, 5], [0, 2, 10], [2, 1, 15]]) == 2
    assert settlingDebts([[0, 1, 20], [0, 2, 10], [2, 1, 15], [
                         0, 3, 5], [3, 1, 10], [3, 2, 15]]) == 3
    assert settlingDebts([[0, 1, 20], [0, 2, 10], [2, 1, 15], [0, 3, 5], [
                         3, 1, 10], [3, 2, 15], [0, 4, 5], [4, 1, 10], [4, 2, 15]]) == 4
    assert settlingDebts([[0, 1, 20], [0, 2, 10], [2, 1, 15], [0, 3, 5], [3, 1, 10], [
                         3, 2, 15], [0, 4, 5], [4, 1, 10], [4, 2, 15], [0, 5, 10], [5, 1, 15], [5, 2, 20]]) == 5


if __name__ == '__main__':
    test_settlingDebt()
