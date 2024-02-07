class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""

        s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        p = [0] * n
        center = right_max = 0

        for i in range(n):
            print(s_prime[i], i, p[i])
            mirror = 2*center - i
            if i < right_max and i + p[mirror] < right_max:
                p[i] = p[mirror]
            
            left = i - p[i] - 1
            right = i + p[i] + 1 
            while right < n and left >= 0 and s_prime[left] == s_prime[right]:
                p[i] += 1
                right += 1
                left -= 1
            
            if i + p[i] > right_max:
                center, right_max = i, i + p[i] 

        max_len, center_index = max((n, i) for i, n in enumerate(p))
        start = (center_index - max_len) // 2
        return s[start: start + max_len]
