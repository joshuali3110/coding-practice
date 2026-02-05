# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        cols = [0] * 9
        boxes = [0] * 9

        for i in range(n):
            row = 0
            for j in range(n):
                if board[i][j] == '.':
                    continue

                mask = 1 << (int(board[i][j]) - 1)
                if row & mask:
                    return False
                row |= mask

                if cols[j] & mask:
                    return False
                cols[j] |= mask

                if boxes[(i // 3) * 3 + (j // 3)] & mask:
                    return False
                boxes[(i // 3) * 3 + (j // 3)] |= mask
        
        return True