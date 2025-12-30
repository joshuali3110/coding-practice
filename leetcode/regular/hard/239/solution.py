# https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque()
        res = []

        for i in range(len(nums)):
            while st and st[-1] < nums[i]:
                st.pop()
            st.append(nums[i])

            if i >= k:
                if nums[i - k] == st[0]:
                    st.popleft()
            if i + 1 >= k:
                res.append(st[0])
        
        return res
            
