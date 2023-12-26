from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        uniqueTriplets = set()
        duplicateValues = set()
        twoSumMap = {}

        for i, firstNum in enumerate(nums):
            if firstNum not in duplicateValues:
                duplicateValues.add(firstNum)
                for j, secondNum in enumerate(nums[i+1:]):
                    thirdNum = -firstNum - secondNum
                    if thirdNum in twoSumMap and twoSumMap[thirdNum] == i:
                        triplet = tuple(sorted((firstNum, secondNum, thirdNum)))
                        uniqueTriplets.add(triplet)
                    twoSumMap[secondNum] = i

        return list(uniqueTriplets)
