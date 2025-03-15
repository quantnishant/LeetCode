class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_table = {}
        for i in range(len(nums)):
            if nums[i] in freq_table:
                freq_table[nums[i]] += 1
            else:
                freq_table[nums[i]] = 1
            if freq_table[nums[i]] > len(nums) // 2:
                return nums[i]