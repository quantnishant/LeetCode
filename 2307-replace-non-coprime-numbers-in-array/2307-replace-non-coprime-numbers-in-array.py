import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            gcd_val = math.gcd(nums[i], nums[i + 1])
            if gcd_val != 1:
                temp = math.lcm(nums[i], nums[i + 1])
                nums.pop(i)  
                nums.pop(i) 
                nums.insert(i, temp)  
                if i > 0:
                    i -= 1
            else:
                i += 1
        return nums