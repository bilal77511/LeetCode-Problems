class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        left_set = set()  # Characters to the left
        right_count = [set() for _ in range(n)]  # Characters to the right

#        print(f"Initial string: {s}")
#        print(f"Length of string: {n}")

        # Precompute the right set for each index
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            right_count[i] = seen.copy()
#            print(f"After processing index {i} (character: '{s[i]}'), right_count: {right_count}")

        unique_palindromes = set()

        # Iterate and count palindromic subsequences
        for i in range(1, n - 1):  # Treat s[i] as the middle character
#            print(f"\nConsidering middle character '{s[i]}' at index {i}")
            left_set.add(s[i - 1])
#            print(f"Characters in left_set: {left_set}")
            for char in left_set:  # Characters from the left
                if char in right_count[i + 1]:  # Characters from the right
#                    print("char",char,"right count",right_count[i + 1])
                    palindrome = (char, s[i], char)
#                    print("palindrome",palindrome)
                    unique_palindromes.add(palindrome)
                    print(f"Found palindrome: {palindrome}")
#            print(f"Unique palindromes so far: {unique_palindromes}")

#        print(f"\nFinal unique palindromes: {unique_palindromes}")
        return len(unique_palindromes)
