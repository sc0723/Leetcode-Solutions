class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        
        return i+1