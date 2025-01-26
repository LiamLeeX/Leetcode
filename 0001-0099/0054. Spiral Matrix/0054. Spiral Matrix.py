# /**
#  * @param {number[][]} matrix
#  * @return {number[]}
#  */
# var spiralOrder = function (matrix) {
#   const result = matrix[0];
#   const dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]];
#   let currentDirIdx = 0;
#   let [m, n] = [matrix.length, matrix[0].length];
#   const position = [0, n - 1];
#   let rest = (m - 1) * n;
#   while (rest > 0) {
#     for (let j = 1; j < m; j++) {
#       rest--;
#       position[0] += dirs[currentDirIdx][0];
#       position[1] += dirs[currentDirIdx][1];
#       result.push(matrix[position[0]][position[1]]);
#     }
#     m--;
#     [m, n] = [n, m];
#     currentDirIdx = (currentDirIdx + 1) % 4;
#   }
#   return result;
# };
from typing import List


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom, result = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


so = Solution()
so.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
