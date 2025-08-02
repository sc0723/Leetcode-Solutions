class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = totalSum = nums[0]

        for i in range(1, len(nums)):
            totalSum = max(totalSum + nums[i], nums[i])
            maxSum = max(maxSum, totalSum)

        return maxSum