class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        sorted_nums = sorted(nums)
        max_diff = 0
        for i in range(len(nums)-1):
            diff = sorted_nums[i+1] - sorted_nums[i]
            if diff > max_diff:
                max_diff = diff
        return max_diff
