class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        se=set()
        for i in nums:
            for i in se:
                return True
            se.add(i)
        return False