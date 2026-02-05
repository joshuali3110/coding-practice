# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, idx):
            if board[r][c] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            
            ch = board[r][c]
            board[r][c] = "*"
            for dr, dc in directions:
                new_r, new_c, = r + dr, c + dc

                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] != "*":
                    if dfs(new_r, new_c, idx + 1):
                        return True
            board[r][c] = ch
            
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
    
        return False