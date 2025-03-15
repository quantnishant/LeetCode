class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_table = {}
        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1
            if freq_table[num] > 1:
                return True
        return False