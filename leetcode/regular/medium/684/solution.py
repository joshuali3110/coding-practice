# https://leetcode.com/problems/redundant-connection/description/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        edge_idx = {}

        for i in range(len(edges)):
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])

            edge_idx[(edges[i][0], edges[i][1])] = (i, True)
            edge_idx[(edges[i][1]), edges[i][0]] = (i, False)

        st = [1]
        visited = set([1])

        res_edges = []
        path = [1]

        def dfs(curr, prev):
            for neighbor in adj_list[curr]:
                if neighbor == prev:
                    continue
                
                if neighbor in visited:
                    nxt = neighbor
                    for i in range(len(path) - 1, -1, -1):
                        res_edges.append((path[i], nxt))
                        nxt = path[i]

                        if path[i] == neighbor:
                            return True
                    print("shouldn't be here")

                visited.add(neighbor)
                path.append(neighbor)
                if dfs(neighbor, curr):
                    return True
                path.pop()
            
            return False
        
        if not dfs(1, -1):
            print("shouldn't be here 2")
            return [-1, -1]
        
        max_idx = -1
        res = None

        for i in range(0, len(res_edges)):
            j, use = edge_idx[res_edges[i]]
            if j > max_idx:
                max_idx = j
                if not use:
                    res = (res_edges[i][1], res_edges[i][0])
                else:
                    res = res_edges[i]

        return list(res)