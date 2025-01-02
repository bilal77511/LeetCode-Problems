class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=(sorted(nums1+nums2))
        l=len(a)
        if l%2 == 0:
            dl=int(l/2)
            return (a[dl-1]+a[dl])/2
        else:
            return float((a[l//2]))