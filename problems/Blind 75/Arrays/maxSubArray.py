# Maximum Subarray
# Leetcode 53: https://leetcode.com/problems/maximum-subarray


class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSum = max(maxSum, currentSum)
            
        
        return maxSum