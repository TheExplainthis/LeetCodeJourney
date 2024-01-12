import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.word = ''

class Solution:
    def __init__(self):
        self.root = TrieNode() 
        self.match_words = set()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True
        curr.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
        
        def backtracking(row, col, parent):
            letter = board[row][col]
            curr = parent.children[letter]

            if curr.is_word:
                self.match_words.add(curr.word)
                curr.is_word = False

            board[row][col] = '#'

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset     
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[row]):
                    new_letter = board[new_row][new_col]
                    if new_letter != '#' and new_letter in curr.children:
                        backtracking(new_row, new_col, curr)

            board[row][col] = letter

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] in self.root.children:
                    backtracking(row, col, self.root)
        
        return list(self.match_words)
