class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high = 1, max(candies)
        best = 0
        while low <= high:
            mid = (low + high) // 2 
            temp = [x // mid for x in candies]
            if k <= sum(temp):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best
        