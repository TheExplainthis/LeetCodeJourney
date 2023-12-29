import collections
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = collections.Counter(t)
        window_freq = collections.defaultdict(int)
        valid_chars, required_chars = 0, len(target_freq)
        slow, fast = 0, 0
        min_window, min_window_size = [-1, -1], math.inf

        new_s = [(i, char) for i, char in enumerate(s) if char in target_freq]
        while fast < len(new_s):
            char = new_s[fast][1]
            window_freq[char] = window_freq.get(char, 0) + 1

            if window_freq[char] == target_freq[char]:
                valid_chars += 1

            while slow <= fast and valid_chars == required_chars:
                char = new_s[slow][1]

                start_index = new_s[slow][0]
                end_index = new_s[fast][0]
                window_size = end_index - start_index + 1
                if window_size < min_window_size:
                    min_window_size = window_size
                    min_window = [start_index, end_index]

                window_freq[char] -= 1
                if window_freq[char] < target_freq[char]:
                    valid_chars -= 1
                slow += 1    
            fast += 1    
        start, end = min_window
        return s[start: end+1] if min_window_size != math.inf else ""
