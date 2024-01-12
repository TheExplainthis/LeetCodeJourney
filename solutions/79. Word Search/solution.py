class Solution(object):
    def exist(self, board, word):

        def backracking(row, col, index):
            if index == len(word):
                return True

            if not (0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] != word[index]:
                return False

            board[row][col] = '#'
            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if backracking(row + row_offset, col + col_offset, index + 1):
                    return True
            board[row][col] = word[index]
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if backracking(row, col, 0):
                    return True
        return False
