import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        self.word = word
        def dfs(startIndex, node):
            curr = node
            for i in range(startIndex, len(self.word)):
                if self.word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if self.word[i] not in curr.children:
                        return False
                    curr = curr.children[self.word[i]]
            return curr.is_word
        return dfs(0, self.root)
