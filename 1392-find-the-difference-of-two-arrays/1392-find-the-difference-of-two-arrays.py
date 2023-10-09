class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff = [[],[]]
        for num in nums1:
            if num not in nums2 and num not in diff[0]:
                diff[0].append(num)
        for num in nums2:
            if num not in nums1 and num not in diff[1]:
                diff[1].append(num)
        return diff