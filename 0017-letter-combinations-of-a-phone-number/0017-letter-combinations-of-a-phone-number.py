class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        his={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans=[""] #starig with empty string in a dictonary
        for num in digits:
            temp_ans=[]
            for  sa in ans:
                for k in his[num]:
                    temp_ans.append(sa+k)
            ans=temp_ans
        return ans