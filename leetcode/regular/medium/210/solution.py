# https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = defaultdict(int)
        adj_list = defaultdict(list) # pre req to course

        for course, pre in prerequisites:
            in_degrees[course] += 1
            adj_list[pre].append(course)
        
        order = []
        q = deque()

        for i in range(numCourses):
            if i not in in_degrees or in_degrees[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            order.append(curr)

            if curr in adj_list:
                for neighbor in adj_list[curr]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 0:
                        q.append(neighbor)
        
        if len(order) < numCourses:
            return []
        return order