class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        old = ""
        al = []
        
        for i in s:
            if i in old:
                al.append(len(old))
                old = old[old.index(i) + 1:]  # Continue the substring after the first occurrence of the repeated character
            old += i
        
        al.append(len(old))  # Add the length of the last substring
        
        return max(al) if al else len(s)  # Handle the case where s is empty or single character