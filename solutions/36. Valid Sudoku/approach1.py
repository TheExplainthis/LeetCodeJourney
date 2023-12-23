from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9

        row_sets = [set() for _ in range(BOARD_SIZE)]
        column_sets = [set() for _ in range(BOARD_SIZE)]
        box_sets = [set() for _ in range(BOARD_SIZE)]

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                
                number = board[row][col]
                if number == ".":
                    continue

                box_index = (row // 3) * 3 + col // 3
                if number in row_sets[row] or number in column_sets[col] or number in box_sets[box_index]:
                    return False
                row_sets[row].add(number)
                column_sets[col].add(number)
                box_sets[box_index].add(number)

        return True
