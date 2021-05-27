class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #first = 0 
        #second = 1
        #while second < len(nums):
            #if nums[first] == nums[second]:
                #nums.remove(nums[second])
            #else:
                #first = second
                #second += 1
                
        #return second
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
                
                
duplicate = Solution()
input_list = [1,1,1,2,3,4,5,5,6]
print(duplicate.removeDuplicates(input_list))

