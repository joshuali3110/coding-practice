# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/submissions/

# revised solution, still makes intuitive sense

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        unique_sorted = sorted(counts.keys())

        prev1, prev2, prev3 = (0, 0), (0, 0), (0, 0)

        for p in unique_sorted:
            safe = -1

            if prev1[1] < p - 2:
                safe = prev1[0]
            elif prev2[1] < p - 2:
                safe = prev2[0]
            else:
                safe = prev3[0]
            
            nxt = (max(prev1[0], safe + p * counts[p]), p)

            prev3 = prev2
            prev2 = prev1
            prev1 = nxt
        
        return max(prev1)

