class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            answer = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = answer 
            b = carry
        return a if a < 0x7FFFFFFF else ~(a ^ mask)
