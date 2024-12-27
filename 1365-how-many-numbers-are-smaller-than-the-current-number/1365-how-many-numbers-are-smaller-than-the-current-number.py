class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snum=sorted(nums)       
        new=[]
        for i in nums:
              new.append(snum.index(i))
        
        return new
            
            
            