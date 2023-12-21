import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = collections.defaultdict(list)
        for word in strs:
            char_frequency = [0] * 26
            for char in word:
                char_frequency[ord(char) - ord('a')] += 1
            anagram_groups[tuple(char_frequency)].append(word)
        return list(anagram_groups.values())