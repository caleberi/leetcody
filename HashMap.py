class HashMap:

    def __init__(self):
        self.bucket = {}

    def put(self, key: int, value: int) -> None:
        self.bucket[key] = value

    def get(self, key: int) -> int:
        if key in self.bucket:
            return self.bucket[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.bucket:
            del self.bucket[key]
