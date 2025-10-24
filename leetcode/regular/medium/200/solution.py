# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    res += 1
                    visited.add((i, j))
                    bfs = deque([(i, j)])

                    while bfs:
                        r, c = bfs.popleft()

                        for dr, dc in dirs:
                            new_r, new_c = r + dr, c + dc

                            if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                                bfs.append((new_r, new_c))
                                visited.add((new_r, new_c))

        return res