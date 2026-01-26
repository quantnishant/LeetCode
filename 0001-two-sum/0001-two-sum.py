class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            if target - nums[i] not in temp:
                temp[nums[i]] = i
            elif target - nums[i] in temp:
                return [temp[target - nums[i]], i]