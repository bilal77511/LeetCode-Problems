class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pink=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            pink=nums[-1]
            print(nums.pop())
            if pink in nums:
                nums.remove(pink)
            else:
                return pink


        