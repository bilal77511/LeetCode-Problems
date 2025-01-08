class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n=len(words)
        ans=set()
        for i in range(n):
            for j in range(i+1,n):
                if words[i] in words[j]:
                    ans.add(words[i])
                elif words[j] in words[i]:
                    ans.add(words[j])
        return list(ans)