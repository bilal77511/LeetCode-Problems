class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pink=0
        for i in nums:
            pink = pink^i
        return pink


        