class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisors = 0
        for i in range(1, n+1):
            if i % m == 0:
                divisors += i
        left_out = n*(n+1) // 2  - divisors 

        return left_out - divisors