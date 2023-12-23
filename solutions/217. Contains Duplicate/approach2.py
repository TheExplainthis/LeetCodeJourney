from typing import List

class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        numbers.sort()
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                return True
        return False
