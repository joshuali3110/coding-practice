# https://leetcode.com/problems/sudoku-solver/

# sets are too slow, use bitmasks instead

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = [0] * 9
        col = [0] * 9
        boxes = [0] * 9

        unsolved = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    unsolved.append((i, j))
                else:
                    mask = 1 << (int(board[i][j]) - 1)
                    row[i] |= mask
                    col[j] |= mask
                    boxes[(i // 3) * 3 + (j // 3)] |= mask
        
        def backtrack(idx):
            if idx == len(unsolved):
                return True
            r, c = unsolved[idx]
            box_idx = (r // 3) * 3 + (c // 3)

            used = row[r] | col[c] | boxes[box_idx]

            for i in range(9):
                mask = 1 << i

                if not (mask & used):
                    row[r] |= mask
                    col[c] |= mask
                    boxes[box_idx] |= mask
                    board[r][c] = str(i + 1)

                    if backtrack(idx + 1):
                        return True
                    
                    row[r] ^= mask
                    col[c] ^= mask
                    boxes[box_idx] ^= mask
        
        backtrack(0)
