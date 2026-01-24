    
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 
from typing import  List

nums = [3,2,4]
target=6

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        "Working with hasmaps"
        seen: dict={}
        for i, v in  enumerate(nums):
            remaining = target-v
            if remaining in seen:
                return[seen[remaining],i]
            seen[v]=i
        return[]
        
                
s= Solution()
print(s.twoSum(nums=nums, target=target))