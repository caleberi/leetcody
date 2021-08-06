from collections import OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        """
        LFUCache(int capacity) Initializes the object with the capacity of the data structure.
        """
        self.capacity = capacity
        self.useCounter = OrderedDict()
        self.currentCapacity = 0
        self.cache = {}

    def get(self, key: int) -> int:
        """
        int get(key:int) Gets the value of the key if the key exists in the cache. Otherwise, returns - 1.
        """
        if key in self.cache:  # check if the key is in cache
            # increment the use count of key to make it the most recently used
            self.useCounter[key] += 1
            self.useCounter.move_to_end(key)
            # update the least recently used key  for the class for quick access
            return self.cache[key]  # return the value of the key
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if self.currentCapacity < self.capacity:
            self.insertIntoCache(key, value)
        else:
            if key in self.cache:
                self.updateKeyInCache(key, value)
                return
            else:
                keyToRemove = self.getLeastUsedKey()
                if keyToRemove == -1:
                    return
                self.updateRecentlyUsed(keyToRemove)
                self.insertIntoCache(key, value)

    def insertIntoCache(self, key, value):
        if key not in self.cache:
            self.cache[key] = value
            self.currentCapacity += 1
            self.useCounter[key] = 1
            self.useCounter.move_to_end(key)
        else:
            self.updateKeyInCache(key, value)

    def updateKeyInCache(self, key, value):
        self.cache[key] = value
        self.useCounter[key] += 1
        self.useCounter.move_to_end(key)

    def getLeastUsedKey(self):
        leastUsedKey = float("inf")
        leastUsedCount = float("inf")
        for key, val in self.useCounter.items():
            if val < leastUsedCount:
                leastUsedCount = val
                leastUsedKey = key
        return leastUsedKey if leastUsedKey != float("inf") else -1

    def updateRecentlyUsed(self, key):
        if key in self.cache and key in self.useCounter:
            del self.cache[key]
            del self.useCounter[key]
            self.currentCapacity -= 1
