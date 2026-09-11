# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        dp = [[1] + [0] * (2**n - 1) for i in range(41)]

        prefs = defaultdict(list)

        for i, likes in enumerate(hats):
            for h in likes:
                prefs[h].append(i)

        for hat in range(1, 41):
            for mask in range(1, 2**n):
                ways = dp[hat-1][mask]

                for person in prefs[hat]:
                    if mask & (1 << person):
                        ways += dp[hat-1][mask & ~(1 << person)]
                        ways %= (10**9 + 7)
                dp[hat][mask] = ways

        return dp[-1][-1]
