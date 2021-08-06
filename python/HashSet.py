class HashSet:

    def __init__(self):
        self.bucket = [None for _ in range(100000)]

    def hashFunc(self, key):
        return key % len(self.bucket)

    def add(self, key: int) -> None:
        hash = self.hashFunc(key)
        if self.bucket[hash] != None:
            return
        else:
            self.bucket[hash] = key

    def remove(self, key: int) -> None:
        hash = self.hashFunc(key)
        if self.bucket[hash] == None:
            return
        else:
            self.bucket[hash] = None

    def contains(self, key: int) -> bool:
        hash = self.hashFunc(key)
        if self.bucket[hash] != None:
            return True
        else:
            return False
