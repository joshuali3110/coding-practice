# https://leetcode.com/problems/count-palindromic-subsequences/description/

class Solution:
    def countPalindromes(self, s: str) -> int:
        singles = defaultdict(int)
        pairs = defaultdict(int)
        running_pairs = []

        for i in range(len(s)):
            for prev, count in singles.items():
                pairs[prev + s[i]] += count
            singles[s[i]] += 1
            running_pairs.append(pairs.copy())
        
        singles = defaultdict(int)
        reverse_pairs = defaultdict(int)
        palindromes = 0

        for i in range(len(s) - 1, -1, -1):
            if i >= 2:
                for rev_pair, count in reverse_pairs.items():
                    palindromes += count * running_pairs[i - 1][rev_pair]
            for prev, count, in singles.items():
                reverse_pairs[prev + s[i]] += count
            singles[s[i]] += 1
            palindromes %= (10**9 + 7)
        
        return palindromes