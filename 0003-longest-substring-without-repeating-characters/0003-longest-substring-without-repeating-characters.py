class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        left = 0
        right = 0
        if len(s) == 0:
            return 0
        while right < len(s) - 1:
            if s[right+1] not in s[left:right+1]:
                
                count = max(right-left +1, count)
                right = right +1 
            else:
                left = left + 1
                right = left
        return count + 1