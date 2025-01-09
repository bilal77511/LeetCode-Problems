class Solution:
    def isPrefixAndSuffix(self,str1:str, str2:str) -> bool:
        if str2.startswith(str1) and str2.endswith(str1):
            #print("true",str1,str2)
            return True
        else:
            #print("false",str1,str2)
            return False
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    count+=1
        return count