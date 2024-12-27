class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        diff=sum(range(len(nums)+1))-sum(nums)
        return diff
            