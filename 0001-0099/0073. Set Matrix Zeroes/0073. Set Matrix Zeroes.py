from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.check_boundary(matrix)
        self.mark_zeros(matrix)
        self.apply_zeros(matrix)
        self.update_boundary(matrix)

    def check_boundary(self, matrix):
        self.first_row_has_zero = False
        self.first_col_has_zero = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                self.first_row_has_zero = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                self.first_col_has_zero = True
                break

    def mark_zeros(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

    def apply_zeros(self, matrix):
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

    def update_boundary(self, matrix):
        if self.first_row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if self.first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


so = Solution()
so.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
