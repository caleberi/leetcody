from random import randint


class RandomizedSet:
    def __init__(self):
        self.store = {}
        self.nums = []

    def insert(self, val):
        if val in self.store:
            return False
        else:
            self.nums.append(val)
            self.store[val] = len(self.nums)-1
            return True

    def remove(self, val):
        if val in self.store:
            if self.store[val] == len(self.nums)-1:
                self.store.pop(val)
                self.nums.pop()
            else:
                dx = self.store[val]
                self.store.pop(val)
                last = self.nums[-1]
                self.nums[dx] = last
                self.nums.pop()
                self.store[last] = dx
            return True
        else:
            return False

    def getRandom(self):
        idx = randint(0, len(self.nums)-1)
        return self.nums[idx]
