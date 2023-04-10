#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            other_index = nums_dict.get(target - num, False)
            if other_index and i != other_index:
                return [i, other_index]


# @lc code=end
