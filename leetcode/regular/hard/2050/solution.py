# https://leetcode.com/problems/parallel-courses-iii/description/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = [[] for _ in range(n)]

        for a, b in relations:
            adj_list[a - 1].append(b - 1)

        times = {}

        def dfs(curr):
            time_after = 0

            for neighbor in adj_list[curr]:
                if neighbor in times:
                    time_after = max(time_after, times[neighbor])
                else:
                    time_after = max(time_after, dfs(neighbor))
            
            times[curr] = time_after + time[curr]
            return times[curr]
        
        res = 0
        for i in range(n):
            if i not in times:
                res = max(res, dfs(i))
        
        return res


        