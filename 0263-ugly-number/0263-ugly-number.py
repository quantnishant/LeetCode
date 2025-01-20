class Solution:
    def isUgly(self, n: int) -> bool:
        if n <=0:
            return False
        for fact in [2, 3, 5]:
            while n % fact == 0:
                n = n // fact
        if n == 1:
            return True
        else:
            return False