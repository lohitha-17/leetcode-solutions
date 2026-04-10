class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            if current_sum <0:
                current_sum = 0
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
            
        return max_sum    
    

#test
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 