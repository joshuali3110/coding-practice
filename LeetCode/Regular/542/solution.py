# https://leetcode.com/problems/01-matrix/description/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        while q:
            r, c = q.popleft()

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r, new_c = r + dx, c + dy

                if 0 <= new_r < m and 0 <= new_c < n and mat[new_r][new_c] > mat[r][c] + 1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    q.append((new_r, new_c))
        
        return mat
        