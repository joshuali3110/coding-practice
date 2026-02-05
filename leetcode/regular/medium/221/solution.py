# https://leetcode.com/problems/maximal-square/description/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        res = 0

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0]:
                res = 1
        
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j]:
                res = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    res = max(res, dp[i][j])
        
        return res**2