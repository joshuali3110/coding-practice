# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []

        for x, y in points:
            d = sqrt(x**2 + y**2)
            heapq.heappush(hp, (-d, x, y))

            if len(hp) > k:
                heapq.heappop(hp)
        
        return [(x, y) for d, x, y in hp]