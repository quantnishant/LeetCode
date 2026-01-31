class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i , j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i = i + 1
            elif nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j = j + 1
        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        mid = len(merged) // 2
        n = len(merged)
        if n % 2 == 0:
            return (merged[mid-1] + merged[mid]) / 2
        else:
            return merged[mid]