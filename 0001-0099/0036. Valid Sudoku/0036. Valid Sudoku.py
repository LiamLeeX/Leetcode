from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track numbers in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                # Calculate which 3x3 box we're in (0-8)
                box_idx = (i // 3) * 3 + j // 3
                # Check if number already exists in row, column, or box
                if (num in rows[i] or
                        num in cols[j] or
                        num in boxes[box_idx]):
                    return False

                # Add number to appropriate sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                box_idx = (i // 3) * 3 + j // 3
                if (num in rows[i] or
                        num in cols[j] or
                        num in boxes[box_idx]):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        return True

so = Solution()
so.isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])