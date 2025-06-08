class Solution:
    def sum_of_digits(self, n: int) -> int:
        return sum(int(digit) for digit in str(n))
    
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == self.sum_of_digits(nums[i]):
                return i
        return -1