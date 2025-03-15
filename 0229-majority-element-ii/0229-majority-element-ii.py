class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_table = {}
        threshold = len(nums) // 3
        final_res = []
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1
            if freq_table[num] > threshold and num not in final_res:
                final_res.append(num)
        return final_res