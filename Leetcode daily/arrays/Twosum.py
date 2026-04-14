class Solution:
    from typing import List
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i
            """
Problem: Two Sum

Approach:
We use a hashmap to store previously seen numbers.

For each element:
- Compute complement = target - current number
- Check if complement exists in hashmap
- If yes, return indices
- Otherwise store current number

Why this works:
Hashmap allows O(1) lookup, reducing time complexity from O(n^2) to O(n)

Time Complexity: O(n)
Space Complexity: O(n)
"""
