# https://leetcode.com/problems/first-completely-painted-row-or-column/description/

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [0] * m
        cols = [0] * n
        pos = {}

        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)

        
        for i in range(m * n):
            r, c = pos[arr[i]]
            rows[r] += 1
            if rows[r] == n:
                return i
            
            cols[c] += 1
            if cols[c] == m:
                return i
            
        return -1