from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True

            elif target < matrix[row][col]:
                col -= 1

            elif target > matrix[row][col]:
                row += 1

        return False


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        for row in matrix:
            if row[0] <= target <= row[n - 1]:
                if any([x == target for x in row]):
                    return True

        return False


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        for row in matrix:
            if row[0] <= target <= row[n - 1]:
                idx = bisect.bisect_left(row, target)
                if row[idx] == target:
                    return True

        return False

