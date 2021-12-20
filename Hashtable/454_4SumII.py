# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l)
# such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dic={}
        count=0
        for num1 in nums1:
            for num2 in nums2:
                if num1+num2 in dic:
                    dic[num1+num2]+=1
                else:
                    dic[num1+num2]=1

        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in dic:
                    count +=dic[-(num3+num4)]
        return count
