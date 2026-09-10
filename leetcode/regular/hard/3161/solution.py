# https://leetcode.com/problems/block-placement-queries/

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        N = max(q[1] for q in queries) + 1

        tree = [0] * (2 * N)

        results = []

        def update(i, val):
            i += N
            tree[i] = val

            while i > 1:
                i //= 2
                tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        
        def query(left, right):
            left += N
            right += N
            res = 0

            while right > left:
                if left % 2 == 1:
                    res = max(res, tree[left])
                    left += 1
                if right % 2 == 1:
                    right -= 1
                    res = max(res, tree[right])
                left //= 2
                right //= 2
            
            return res
        
        blocks = SortedList([0])

        for q in queries:
            if q[0] == 1:
                ins = blocks.bisect(q[1])
                update(q[1], q[1] - blocks[ins - 1])

                if ins < len(blocks):
                    update(blocks[ins], blocks[ins] - q[1])
                
                blocks.add(q[1])
            else:
                idx = blocks.bisect(q[1])
                results.append(max(q[1] - blocks[idx-1], query(0, blocks[idx - 1] + 1)) >= q[2])
                
        return results
            
        