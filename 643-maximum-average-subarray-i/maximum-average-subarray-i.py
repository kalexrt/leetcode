class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum += nums[i]
        maxSum = currSum # assume max sum is the sum of first 'k' elements
        left = 0
        right = k
        while right < len(nums): 
            currSum -= nums[left] 
            left += 1 
            currSum += nums[right] 
            right += 1 
            maxSum = max(maxSum, currSum) 
        return maxSum / k 
