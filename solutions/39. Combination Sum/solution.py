from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start_index, remaining, current_combination):
            if remaining == 0:
                result.append(list(current_combination))
                return
            if remaining < 0:
                return

            for i in range(start_index, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, remaining - candidates[i], current_combination)
                current_combination.pop()

        backtrack(0, target, [])
        return result
