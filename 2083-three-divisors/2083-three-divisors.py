class Solution:
    def isThree(self, n: int) -> bool:
        divisors_count = 0
        for i in range(1, int(math.sqrt(n)+1)):
            if n % i == 0 and i != n//i:
                divisors_count += 2
            elif n % i == 0 and i == n//i:
                divisors_count += 1
        return divisors_count == 3