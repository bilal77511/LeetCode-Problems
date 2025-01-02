class Solution:
    def reverse(self, x: int) -> int:
        result=0
        maxi,mini=-2**31, 2**31 - 1
        isnegative= x < 0
        x=abs(x)

        while x!=0:
            digit=x%10
            x=x//10
            if result > (mini - digit)//10:
                return 0
            result=result * 10+ digit
        if isnegative:
            result = -1 *result
        return result if maxi<= result <= mini else 0