class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = {}
        max_length = 0
        slow = 0
        
        for fast in range(len(s)):
            if s[fast] in unique_chars:
                slow = max(unique_chars[s[fast]], slow)
            unique_chars[s[fast]] = fast + 1
            max_length = max(max_length, fast - slow + 1)
        return max_length
