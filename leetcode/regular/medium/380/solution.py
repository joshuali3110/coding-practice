# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        
        self.d[val] = len(self.l)
        self.l.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        pos = self.d[val]
        del self.d[val]
        self.l[pos] = self.l[-1]
        self.l.pop()

        if pos < len(self.l):
            self.d[self.l[pos]] = pos

        return True


    def getRandom(self) -> int:
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()