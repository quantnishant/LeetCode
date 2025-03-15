class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_table = {}
        threshold = len(nums) // 2 
        
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1
            if freq_table[num] > threshold:
                return num