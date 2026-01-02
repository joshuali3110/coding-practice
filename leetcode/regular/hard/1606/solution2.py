# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description/

# two heap approach, storing index of next task that this server "wants" in free list

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
                distance = server - i % k
                if server < i % k:
                    distance += k
                heappush(free, i + distance)

            if len(free) == 0:
                continue

            use = heappop(free) % k

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