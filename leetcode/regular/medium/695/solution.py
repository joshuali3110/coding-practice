# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs = deque([(i, j)])
                    grid[i][j] = 0
                    size = 0

                    while bfs:
                        r, c = bfs.popleft()
                        size += 1
                        for dr, dc in dirs:
                            new_r, new_c = r + dr, c + dc
                            
                            if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                                grid[new_r][new_c] = 0
                                bfs.append((new_r, new_c))
                    
                    res = max(res, size)

        return res