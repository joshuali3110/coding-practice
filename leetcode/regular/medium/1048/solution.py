# https://leetcode.com/problems/longest-string-chain/description/

# approach for finding predecessor relationships involved checking every pair of strings (O(m^2) for 1 <= m <= 1000), where each check is O(string length) (1 <= n <= 16); bairly passed TLE (beat 5%); O(m^2 * n)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        adj_list = {}

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.isPredecessor(words[i], words[j]):
                    if i not in adj_list:
                        adj_list[i] = []
                    adj_list[i].append(j)
                elif self.isPredecessor(words[j], words[i]):
                    if j not in adj_list:
                        adj_list[j] = []
                    adj_list[j].append(i)

        found = {}
        def dfs(curr):
            longest = 0

            if curr in adj_list:
                for neighbor in adj_list[curr]:
                    if neighbor in found:
                        longest = max(longest, found[neighbor])
                    else:
                        longest = max(longest, dfs(neighbor))
            
            found[curr] = 1 + longest
            return found[curr]
        
        res = 0
        for i in range(len(words)):
            if i not in found:
                res = max(res, dfs(i))
        
        return res

    def isPredecessor(self, pre, curr):
        if len(curr) != len(pre) + 1:
            return False
        
        for i in range(len(pre)):
            if pre[i] != curr[i]:
                return pre[i:] == curr[i+1:]
        
        return True