class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = [ch.lower() for ch in s if ch.isalnum()]
        return clean_chars == clean_chars[::-1]
