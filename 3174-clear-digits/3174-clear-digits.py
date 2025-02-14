class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        digit="0123456789"
        for i in s:
            if stack and i in digit:
                stack.pop()
            elif i not in digit:
                stack.append(i)
        return "".join(stack)