# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         l = len(nums)
#         anslis = [0] * l
#         anslis[0] = nums[0]
#         for i in range(1, l):
#             anslis[i] = anslis[i - 1] + nums[i]


#         tot = sum(nums)
#         ans = 0
#         for l in anslis[: l - 1]:
#             r = tot - l
#             if l >= r:
#                 ans += 1
#         return ans
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0  # Running sum of the left part
        valid_splits = 0  # Count of valid splits

        # Iterate through the array except the last element
        for i in range(len(nums) - 1):
            left_sum += nums[i]  # Update left sum
            right_sum = total_sum - left_sum  # Calculate right sum
            if left_sum >= right_sum:  # Check validity of the split
                valid_splits += 1

        return valid_splits
