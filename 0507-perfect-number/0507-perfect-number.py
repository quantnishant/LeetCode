import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        temp_list = [1]
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                temp_list.append(i)
                if i != num // i:
                    temp_list.append(num // i)

        return sum(temp_list) == num