from typing import List
from collections import Counter
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = Counter(nums)
        unique_nums = list(num_frequencies.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_freq = num_frequencies[unique_nums[pivot_index]]

            unique_nums[pivot_index], unique_nums[right] = unique_nums[right], unique_nums[pivot_index]  

            store_index = left
            for i in range(left, right):
                if num_frequencies[unique_nums[i]] < pivot_freq:
                    unique_nums[store_index], unique_nums[i] = unique_nums[i], unique_nums[store_index]
                    store_index += 1

            unique_nums[right], unique_nums[store_index] = unique_nums[store_index], unique_nums[right]  
            return store_index
        
        def quickselect(left, right, target_index) -> None:
            if left == right: 
                return
            
            pivot_index = random.randint(left, right)     
            pivot_index = partition(left, right, pivot_index)
            
            if target_index == pivot_index:
                return 
            elif target_index < pivot_index:
                quickselect(left, pivot_index - 1, target_index)
            else:
                quickselect(pivot_index + 1, right, target_index)
         
        num_elements = len(unique_nums) 
        quickselect(0, num_elements - 1, num_elements - k)
        return unique_nums[num_elements - k:]
