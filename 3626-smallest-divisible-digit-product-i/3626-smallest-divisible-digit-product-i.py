class Solution:
    def prod_dig(self, n):
        prod = 1
        for i in str(n):
            prod *= int(i)
        return prod
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while i >= n:
            if self.prod_dig(i) % t == 0:
                return i
            else:
                i += 1