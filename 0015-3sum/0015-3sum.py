class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        ans = []
        n = len(nums)

        for i in range(n - 2):  # Step 2: Fix the first number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for the first number
                continue
            
            target = -nums[i]
            left, right = i + 1, n - 1  # Two-pointer setup
            
            while left < right:  # Step 3: Find two numbers that sum to `target`
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    ans.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward
                    left += 1
                    right -= 1
                elif current_sum < target:  # Sum too small, move left pointer
                    left += 1
                else:  # Sum too large, move right pointer
                    right -= 1

        return ans