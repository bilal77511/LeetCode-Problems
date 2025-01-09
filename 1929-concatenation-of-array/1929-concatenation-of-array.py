class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans=nums+nums
        # return ans
        ans=[]
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans