from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.mark_cells(board)
        self.update_cells(board)

    def mark_cells(self, board):
        # First pass: Mark cells that will change
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = self.count_neighbors(board, i, j)
                if board[i][j] == 1:
                    # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 3  # Will die
                else:
                    # Dead cell
                    if live_neighbors == 3:
                        board[i][j] = 2  # Will become alive

    def count_neighbors(self, board,row: int, col: int) -> int:
        neighbors = 0
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                if (i != row or j != col) and board[i][j] % 2:
                    # 0 % 2 = 0(死细胞)
                    # 1 % 2 = 1(活细胞)
                    # 2 % 2 = 0(原来是死细胞)
                    # 3 % 2 = 1(原来是活细胞)
                    neighbors += 1
        return neighbors

    def update_cells(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

so = Solution()
so.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        self.mark_cells(board)
        self.update_cells(board)

    def mark_cells(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = self.count_neighbors(board, i, j)
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 3
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2

    def count_neighbors(self, board,row: int, col: int) -> int:
        neighbors = 0
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                if (i != row or j != col) and board[i][j] % 2:
                    neighbors += 1
        return neighbors

    def update_cells(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
