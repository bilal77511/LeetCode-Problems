class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l=len(nums)
        anslis=[0]*l
        anslis[0]=nums[0]
        for i in range(1,l):
            anslis[i]=anslis[i-1]+nums[i]
        
        tot=sum(nums)
        ans=0
        for l in anslis[:l-1]:
            r=tot-l
            if l>=r:
                ans+=1
        return ans
        