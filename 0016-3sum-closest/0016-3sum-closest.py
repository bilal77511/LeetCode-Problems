class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n= len(nums)
        if n == 3:
            return sum(nums)
        nums.sort()
        real_ans=float('inf')
        for i in range(n-2):
            left=i+1
            right=n-1
            while left < right:
                current_sum=nums[i]+nums[left]+nums[right]
                if abs(current_sum - target) < abs(real_ans- target):
                    real_ans = current_sum
                if current_sum < target:
                    left=left+1
                elif current_sum > target:
                    right-=1
                else:
                    return current_sum
        return real_ans
                