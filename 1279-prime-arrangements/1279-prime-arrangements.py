import math
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def count_primes(n):
            if n < 2:
                return 0
            is_prime = [True] * n
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n, i):
                        is_prime[j] = False
            return sum(is_prime)
        a = count_primes(n+1)
        return math.factorial(a)*math.factorial(n-a) % (10**9 + 7)
        