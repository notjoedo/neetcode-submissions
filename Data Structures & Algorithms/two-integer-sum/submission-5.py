class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this is an o(n^2) solution:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target and i!=j):
                    return [i,j];
        