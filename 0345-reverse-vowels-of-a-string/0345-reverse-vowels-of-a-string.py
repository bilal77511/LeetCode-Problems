class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        vow="aeiouAEIOU"
        ans=list(s)
        while (l<r):
            if ans[l] not in vow:
                l+=1
            elif ans[r] not in vow:
                r-=1
            else:
                ans[r],ans[l]=ans[l],ans[r]
                r=r-1
                l=l+1
        return "".join(ans)