# https://leetcode.com/problems/couples-holding-hands/description/

# greedy solution that simply keeps making swaps; greedy approach intuition (and proof) comes from the graph understanding of the problem

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        pos = {}

        for i in range(2 * n):
            pos[row[i]] = i
        
        res = 0
        for i in range(0, 2 * n, 2):
            swap = pos[row[i]^1]
            row[i+1], row[swap] = row[swap], row[i+1]
            pos[row[i+1]] = i+1
            pos[row[swap]] = swap
            res += i+1!=swap
        
        return res