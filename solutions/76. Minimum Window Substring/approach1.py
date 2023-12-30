import collections
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = collections.Counter(t)
        window_freq = collections.defaultdict(int)
        valid_chars, required_chars = 0, len(target_freq)
        slow, fast = 0, 0
        min_window, min_window_size = [-1, -1], math.inf
        
        while fast < len(s):
            char_at_end = s[fast]
            window_freq[char_at_end] += 1
            
            if char_at_end in target_freq and window_freq[char_at_end] == target_freq[char_at_end]:
                valid_chars += 1

            while valid_chars == required_chars:
                current_window_size = fast - slow + 1
                if current_window_size < min_window_size:
                    min_window_size = current_window_size
                    min_window = [slow, fast]
                
                char_at_start = s[slow]
                window_freq[char_at_start] -= 1
                if char_at_start in target_freq and window_freq[char_at_start] < target_freq[char_at_start]:
                    valid_chars -= 1
                slow += 1
            fast += 1
        start, end = min_window
        return s[start: end+1] if min_window_size != math.inf else ""
