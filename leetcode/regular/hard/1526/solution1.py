# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        st = []
        ops = 0

        for height in target:
            if not st:
                st.append(height)
                ops += height
            else:
                if height >= st[-1]:
                    ops += height - st[-1]
                else:
                    while st and st[-1] > height:
                        st.pop()

                st.append(height)
        
        return ops