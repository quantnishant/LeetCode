from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        return sorted(freq_table, key = freq_table.get, reverse = True)[:k]