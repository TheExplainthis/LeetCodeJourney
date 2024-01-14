from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        queue = deque([char for char in indegree if indegree[char] == 0])
        alien_dict_order = ""

        while queue:
            char = queue.popleft()
            alien_dict_order += char
            for next_char in adj_list[char]:
                indegree[next_char] -= 1
                if indegree[next_char] == 0:
                    queue.append(next_char)

        if len(alien_dict_order) != len(indegree):
            return ""  

        return alien_dict_order
