class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 > x or x > 2**31 - 1:
            return 0
        else:
            if x >= 0:
                if int(str(x)[::-1]) < 2**31:
                    return int(str(x)[::-1]) 
                else:
                    return 0 
            elif x < 0:
                stri = str(x)[1:]
                if -int(stri[::-1]) > -2**31:
                    return -int(stri[::-1]) 
                else:
                    return 0
