from typing import List, Set

class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        seen: Set[int] = set()
        for number in numbers:
            if number in seen:
                return True
            seen.add(number)
        return False
