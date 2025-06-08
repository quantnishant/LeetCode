class Solution:
    def gcd(self, a, b):
        while b != 0:
            a , b = b , a % b 
        return a
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(max(nums), min(nums))