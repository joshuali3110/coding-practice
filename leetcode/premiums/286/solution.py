from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.pop()

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < m and 0 <= new_c < n and rooms[new_r][new_c] != -1:
                    if rooms[new_r][new_c] > rooms[r][c] + 1:
                        rooms[new_r][new_c] = rooms[r][c] + 1
                        q.append((new_r, new_c))
        

