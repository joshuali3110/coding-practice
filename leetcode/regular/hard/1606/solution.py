# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description/

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = [x for x in range(k)]
        completed = [0] * k
        end_times = []
        time = 0

        for i in range(len(arrival)):
            time = arrival[i]

            while end_times and end_times[0][0] <= time:
                _, server = heappop(end_times)
                completed[server] += 1
                free.insert(bisect_right(free, server), server)

            if len(free) == 0:
                continue

            lookup = bisect_right(free, i % k)

            if lookup > 0 and free[lookup - 1] == i % k:
                use = free.pop(lookup - 1)
            else:
                if lookup == len(free):
                    lookup = 0
                
                use = free.pop(lookup)

            heappush(end_times, (time + load[i], use))

        for _, server in end_times:
            completed[server] += 1
        
        res = []
        busiest = -1
        for i in range(k):
            if completed[i] > busiest:
                res = [i]
                busiest = completed[i]
            elif completed[i] == busiest:
                res.append(i)
        
        return res