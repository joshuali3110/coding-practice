# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        def palindromesAround(center):
            nonlocal palindromes
            left = center
            right = center

            while right < len(s) and left >= 0:
                if s[left] == s[right]:
                    palindromes += 1
                else:
                    break
                left -= 1
                right += 1
            
            left = center
            right = center + 1
            
            while right < len(s) and left >= 0:
                if s[left] == s[right]:
                    palindromes += 1
                else:
                    break
                left -= 1
                right += 1
        
        for i in range(len(s)):
            palindromesAround(i)
        
        return palindromes
            