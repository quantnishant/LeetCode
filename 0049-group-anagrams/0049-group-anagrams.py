class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = {}
        for strings in strs:
            sorted_str = ''.join(sorted(strings))
            if sorted_str not in temp_dict:
                temp_dict[sorted_str] = [strings]
            else:
                temp_dict[sorted_str].append(strings)
        return list(temp_dict.values())
