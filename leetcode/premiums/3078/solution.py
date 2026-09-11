from typing import List

class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        m, n, r, c = len(board), len(board[0]), len(pattern), len(pattern[0])

        def matches(x, y):
            mappings = {}
            mapped_digits = set()

            for i in range(r):
                for j in range(c):
                    if pattern[i][j].isdigit():
                        if int(pattern[i][j]) != board[x+i][y+j]:
                            return False
                    elif pattern[i][j] in mappings:
                        if mappings[pattern[i][j]] != board[x+i][y+j]:
                            return False
                    else:
                        if board[x+i][y+j] in mapped_digits:
                            return False
                        mappings[pattern[i][j]] = board[x+i][y+j]
                        mapped_digits.add(board[x+i][y+j])

            return True

        for i in range(m - r + 1):
            for j in range(n - c + 1):
                if matches(i, j):
                    return [i, j]

        return [-1, -1]