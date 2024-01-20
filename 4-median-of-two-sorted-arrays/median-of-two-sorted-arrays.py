class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2

        merged.sort()

        total = len(merged)

        if (total%2 == 1):
            return float(merged[total // 2])
        else:
            return ((float(merged[total // 2]) + (float(merged[total//2 -1])))/2.0)

        