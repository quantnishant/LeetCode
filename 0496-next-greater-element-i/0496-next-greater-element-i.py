class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for number in nums1:
            ans = -1
            idx_nums2 = nums2.index(number)
            for j in range(idx_nums2 + 1 , len(nums2)):
                if nums2[j] > number:
                    ans = nums2[j]
                    break
            result.append(ans)
        return result