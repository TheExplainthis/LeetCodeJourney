class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31

        while n:
            result += (n & 1) << power
            n = n >> 1
            power -= 1

        return result
