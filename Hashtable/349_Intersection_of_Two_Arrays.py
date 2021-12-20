#Given two integer arrays nums1 and nums2,
# return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set(nums1)
        b = set(nums2)
        return a.intersection(b)