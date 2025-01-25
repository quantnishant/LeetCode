class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        temp_list = [1]
        i = 2
        while len(temp_list) < n:
            result = all((x + i) != k for x in temp_list)
            if result:
                temp_list.append(i)
            i += 1
        return sum(temp_list)