class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res=nums1[:m]+nums2
        res.sort()
        nums1[:]=res
        