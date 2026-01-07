# https://leetcode.com/problems/couples-holding-hands/description/

# solution based on building an adjacency list and finding the number of cycles/sections of graph that exist; each cycle/section will end up with a swap that will create two correct pairs (subtract one from total number of couples)

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2

        pos = {}

        for i in range(len(row)):
            pos[row[i]] = i

        adj_list = defaultdict(list)

        for i in range(0, 2 * n, 2):
            c1 = pos[i] // 2
            c2 = pos[i + 1] // 2
            adj_list[c1].append(c2)
            adj_list[c2].append(c1)
        
        found = set()
        def dfs(curr):
            for neighbor in adj_list[curr]:
                if neighbor not in found:
                    found.add(neighbor)
                    dfs(neighbor)
        
        cycles = 0
        for i in range(n):
            if i not in found:
                cycles += 1
                found.add(i)
                dfs(i)

        return n - cycles
                