class Solution:
    def myAtoi(self, s: str) -> int:
        k = ""
        
        # Edge case: if the input is just "+" or "-", or empty
        if s == "+" or s == "-" or not s:
            return 0
        
        # Iterate through the string
        for i in s:
            # Ignore leading spaces
            if i == " " and not k:
                continue
            
            # Handle '-' sign
            elif i == "-" and not k:
                k += i
            
            # Handle invalid '-' after digits or signs
            elif i == "-" and k:
                return int(k) if k not in ["+", "-"] else 0
            
            # Handle '+' sign
            elif i == "+" and not k:
                k += i
            
            # Handle invalid '+' after digits or signs
            elif i == "+" and k:
                return int(k) if k not in ["+", "-"] else 0
            
            # Add digits to the result
            elif i in "0123456789":
                k += i
            
            # Stop on encountering non-digit characters
            else:
                break
        
        # Handle cases where k is empty or just a sign
        if not k or k in ["+", "-"]:
            return 0
        
        # Convert k to an integer
        k = int(k)
        
        # Clamp the result to 32-bit signed integer range
        return max(min(k, (2**31) - 1), -(2**31))