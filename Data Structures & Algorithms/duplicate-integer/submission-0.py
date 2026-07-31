class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for digit in nums:
            if digit in hashset:
                return True
            hashset.add(digit)
        return False
