from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9

        row_flags = [0] * BOARD_SIZE
        col_flags = [0] * BOARD_SIZE
        box_flags = [0] * BOARD_SIZE

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == ".":
                    continue

                number = int(board[row][col]) - 1
                bit_flag = 1 << number

                box_index = (row // 3) * 3 + col // 3
                if row_flags[row] & bit_flag or col_flags[col] & bit_flag or box_flags[box_index] & bit_flag:
                    return False

                row_flags[row] |= bit_flag
                col_flags[col] |= bit_flag
                box_flags[box_index] |= bit_flag

        return True
