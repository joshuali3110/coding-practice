from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        change = True

        while change:
            destroy = set()
            change = False

            # horizontal check
            for i in range(m):
                curr = board[i][0]
                count = 1
                for j in range(1, n):
                    if board[i][j] == curr:
                        count += 1
                    else:
                        curr = board[i][j]
                        count = 1

                    if curr == 0:
                        continue

                    if count == 3:
                        destroy.add((i, j-2))
                        destroy.add((i, j-1))
                        destroy.add((i, j))
                    if count > 3:
                        destroy.add((i, j))

            # vertical check
            for j in range(n):
                curr = board[0][j]
                count = 1
                for i in range(1, m):
                    if board[i][j] == curr:
                        count += 1
                    else:
                        curr = board[i][j]
                        count = 1

                    if curr == 0:
                        continue

                    if count == 3:
                        destroy.add((i-2, j))
                        destroy.add((i-1, j))
                        destroy.add((i, j))
                    if count > 3:
                        destroy.add((i, j))

            if destroy:
                change = True

                for i, j in destroy:
                    board[i][j] = 0

                for j in range(n):
                    bottom = None

                    for i in range(m-1, -1, -1):
                        if board[i][j] == 0:
                            if bottom is None:
                                bottom = i
                        elif bottom is not None:
                            board[bottom][j] = board[i][j]
                            board[i][j] = 0
                            bottom -= 1

        return board
                        