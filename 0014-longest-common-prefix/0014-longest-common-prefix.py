class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        temp = strs[0]
        for i in range(1, len(strs)):
            m = min(len(result), len(strs[i]))
            j = 0
            while strs[i][:j] == temp[:j] and j <=  m:
                result = strs[i][:j]
                j = j + 1
            temp = strs[i][:j-1]
        return result

        