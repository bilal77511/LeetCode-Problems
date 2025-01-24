class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for i in s:
            if s1 and i == "#":
                s1.pop()
            else:
                s1.append(i)
        for j in t:
            if t1 and j=="#":
                t1.pop()
            else:
                t1.append(j)

        return s1==t1