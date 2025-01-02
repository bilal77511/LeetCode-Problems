class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        his={} #his as history
        for i, num in enumerate(nums):
            x= target - num #x is the valuw we have to find
            if x in his:
                return [his[x],i]
            his[num]=i
                