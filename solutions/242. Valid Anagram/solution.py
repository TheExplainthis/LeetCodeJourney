import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = collections.defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in t:
            if char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True
