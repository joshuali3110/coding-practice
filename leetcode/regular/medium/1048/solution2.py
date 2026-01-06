# https://leetcode.com/problems/longest-string-chain/description/

# approach for finding predecessor relationships involves test-deleting every character from each word (O(m^2) for 1 <= m <= 1000) and checking against a set of all words; O(m * n^2) where 1 <= n <= 16, vs O(m^2 * n) for previous solution
# using deletion instead of insertion narrows down possible "neighbors" by a lot; deletion has word[i].length options, while insertion has word[i].length * 26 options

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set()

        for w in words:
            word_set.add(w)

        found = {}

        def dfs(curr):
            longest = 0

            for i in range(len(curr)):
                pre = curr[0:i] + curr[i+1:]
                if pre in word_set:
                    if pre in found:
                        longest = max(longest, found[pre])
                    else:
                        longest = max(longest, dfs(pre))
            
            found[curr] = 1 + longest
            return found[curr]

        res = 0
        for w in word_set:
            if w not in found:
                res = max(res, dfs(w))
        
        return res