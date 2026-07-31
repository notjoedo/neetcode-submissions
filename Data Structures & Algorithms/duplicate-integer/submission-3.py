class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            current = nums[i]
            for j in range(len(nums)):
                if i != j and current == nums[j]:
                    return True
        
        return False