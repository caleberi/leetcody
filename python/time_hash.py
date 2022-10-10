from collections import OrderedDict


class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store : 
            self.store[key][timestamp] = value # in order to store values in timeslots
        else:
            self.store[key] = {timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            for i in reversed(range(1,timestamp+1)):
                if i in self.store[key]:
                    return self.store[key][i]
            return ""
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)