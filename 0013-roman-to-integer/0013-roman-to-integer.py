class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        prev=0
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}# making dict
        for i in s[::-1]:
            c=roman[i]
            if prev <= c:
                total=total + c
            elif prev > c:
                total=total - c
            prev=roman[i]
        return total