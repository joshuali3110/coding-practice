# https://leetcode.com/problems/find-median-from-data-stream/description/

class MedianFinder:

    def __init__(self):
        self.max_hp = [] 
        self.min_hp = [] # always larger or equal

    def addNum(self, num: int) -> None:
        if len(self.max_hp) == len(self.min_hp):
            heappush(self.min_hp, -heappushpop(self.max_hp, -num))
        else:
            heappush(self.max_hp, -heappushpop(self.min_hp, num))

    def findMedian(self) -> float:
        if len(self.max_hp) == len(self.min_hp):
            return (-self.max_hp[0] + self.min_hp[0]) / 2
        else:
            return self.min_hp[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()