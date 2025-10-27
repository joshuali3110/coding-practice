# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        
        idx = bisect_left(self.mp[key], (timestamp, ""))

        if idx == len(self.mp[key]):
            idx -= 1
        elif timestamp == self.mp[key][idx][0]:
            return self.mp[key][idx][1]
        else:
            idx -= 1

        if 0 <= idx < len(self.mp[key]):
            return self.mp[key][idx][1]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)