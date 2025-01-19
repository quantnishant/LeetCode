class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        track = 1
        while track < len(nums):
            if nums[i] == nums[track]:
                del nums[i]
            else:
                i = i + 1
                track += 1
        return len(nums)

