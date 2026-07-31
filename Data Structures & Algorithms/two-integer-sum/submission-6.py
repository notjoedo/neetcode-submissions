class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this is an o(n) solution using hashmaps:
        difference = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in difference:
                return [difference[diff], i]
            difference[n] = i
        