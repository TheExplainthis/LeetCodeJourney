from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_order = []
        total_rows, total_columns = len(matrix), len(matrix[0])
        top_row = left_column = 0
        bottom_row = total_rows - 1
        right_column = total_columns - 1

        while len(spiral_order) < total_rows * total_columns:
            for col in range(left_column, right_column + 1):
                spiral_order.append(matrix[top_row][col])

            for row in range(top_row + 1, bottom_row + 1):
                spiral_order.append(matrix[row][right_column])

            if top_row != bottom_row:
                for col in range(right_column - 1, left_column - 1, -1):
                    spiral_order.append(matrix[bottom_row][col])

            if left_column != right_column:
                for row in range(bottom_row - 1, top_row, -1):
                    spiral_order.append(matrix[row][left_column])

            left_column += 1
            right_column -= 1
            top_row += 1
            bottom_row -= 1

        return spiral_order
