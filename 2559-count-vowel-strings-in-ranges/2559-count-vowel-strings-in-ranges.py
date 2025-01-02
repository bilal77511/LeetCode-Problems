# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#         res=[]
#         ans=[]
#         vowels=tuple("aeiou")
#         for word in words:
#             if word.startswith(vowels) and word.endswith(vowels):
#                 res.append(1)
#             else:
#                 res.append(0)
#         for querie in queries:
#             ans.append(sum(res[querie[0]:querie[1]+1]))
#         return ans
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Step 1: Precompute the validity of words
        vowels = set("aeiou")  # Using set for O(1) lookups
        res = []
        
        for word in words:
            # Check if the word starts and ends with a vowel
            if word[0] in vowels and word[-1] in vowels:
                res.append(1)
            else:
                res.append(0)
        
        # Step 2: Precompute prefix sum for valid words
        prefix_sum = [0] * len(words)
        prefix_sum[0] = res[0]
        
        # Fill in the prefix sum array
        for i in range(1, len(words)):
            prefix_sum[i] = prefix_sum[i - 1] + res[i]
        
        # Step 3: Answer queries in O(1) time using prefix sum
        ans = []
        for query in queries:
            l, r = query
            if l > 0:
                ans.append(prefix_sum[r] - prefix_sum[l - 1])  # Get the sum for the range [l, r]
            else:
                ans.append(prefix_sum[r])  # If l == 0, just take prefix_sum[r]
        
        return ans
