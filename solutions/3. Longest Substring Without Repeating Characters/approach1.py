class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        max_length = 0
        slow = 0
        
        for fast in range(len(s)):
            while s[fast] in unique_chars:
                unique_chars.remove(s[slow])
                slow += 1
            unique_chars.add(s[fast])
            max_length = max(max_length, fast - slow + 1)
        return max_length
