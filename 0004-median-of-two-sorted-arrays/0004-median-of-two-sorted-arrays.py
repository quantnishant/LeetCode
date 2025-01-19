class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0 
        j = 0 
        temp = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i = i + 1 
            else:
                temp.append(nums2[j])
                j = j + 1
    
        temp.extend(nums1[i:])
        temp.extend(nums2[j:])

        
        total_length = len(temp)
        if total_length % 2 == 1:
            return temp[total_length // 2]
        else:
            mid_right = total_length // 2
            mid_left = mid_right - 1
            return float(temp[mid_left] + temp[mid_right]) / 2