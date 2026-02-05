# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        n = len(s)

        for w in wordDict:
            curr = trie
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["*"] = None

        dp = [True] + [False] * n

        for i in range(0, n + 1):
            if not dp[i]:
                continue
            j = i
            curr = trie

            while j < n:
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if "*" in curr:
                    dp[j+1] = True
                j += 1
            
            if dp[-1]:
                return True    

        return dp[-1]