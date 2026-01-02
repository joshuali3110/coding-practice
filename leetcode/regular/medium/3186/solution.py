# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/submissions/

# initial solution, ugly code but intuitively makes more immediate sense to me

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        prev1 = [0, 0]
        prev2 = [0, 0]
        power.sort()
        curr = power[0]
        count = 1

        res = 0

        for i in range(1, len(power)):
            if power[i] == curr:
                count += 1
            else:
                if power[i] > curr + 2:
                    res += max([prev2[1] + curr * count, max([prev1[0], prev1[1], prev2[0]])])
                    prev1 = [0, 0]
                    prev2 = [0, 0]
                else:
                    if power[i] == curr + 2:
                        nxt = [prev2[1] + curr * count, max([prev1[0], prev1[1], prev2[0]])]
                        prev2 = prev1
                        prev1 = nxt
                        curr += 1
                        count = 0
                    nxt = [prev2[1] + curr * count, max([prev1[0], prev1[1], prev2[0]])]
                    prev2 = prev1
                    prev1 = nxt
                curr = power[i]
                count = 1

        return res + max([prev2[1] + curr * count, max([prev1[0], prev1[1], prev2[0]])])