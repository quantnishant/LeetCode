import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        temp = n*(n+1) // 2
        x = int(math.sqrt(temp))
        if x*x == temp:
            return x
        return -1
        