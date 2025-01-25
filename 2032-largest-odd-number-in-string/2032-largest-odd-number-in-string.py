class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(1, n+1):
            if int(num[-i]) % 2 == 1:
                return num[:n-i+1]
                break
        return ''