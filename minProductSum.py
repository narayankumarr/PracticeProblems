class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        sums = 0
        length = len(nums1)        
        for i in range(0, length):
            sums = sums + (nums1[i]*nums2[length-i-1])    
        return sums
