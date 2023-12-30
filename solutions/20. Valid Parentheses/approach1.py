class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for bracket in s:
            if bracket not in matching_brackets:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != matching_brackets[bracket]:
                    return False
        return not stack
