class Solution:
    def isHappy(self, n: int) -> bool:
        def add_square(number):
            temp_list = [int(digit)**2 for digit in str(number)]
            return sum(temp_list)
        while add_square(n) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            n = add_square(n)
        if add_square(n) == 1 or add_square(n) == 7:
            return True
        else:
            return False