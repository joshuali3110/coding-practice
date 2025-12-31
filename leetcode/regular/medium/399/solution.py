# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = {}

        for i in range(len(equations)):
            n1, n2 = equations[i]

            if n1 not in nodes:
                nodes[n1] = {}
            
            if n2 not in nodes:
                nodes[n2] = {}
            
            nodes[n1][n2] = values[i]
            nodes[n2][n1] = 1/values[i]
        
        def dfs(start, target):
            visited = set()
            product = 1

            def helper(curr):
                nonlocal product
            
                if curr == target:
                    return True
                
                for neighbor, weight in nodes[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)

                        product *= weight

                        if helper(neighbor):
                            return True
                        
                        product /= weight
            
            if helper(start):
                return product
            else:
                return -1.0
        
        res = []
        for start, target in queries:
            if start not in nodes or target not in nodes:
                res.append(-1.0)
            else:
                res.append(dfs(start, target))
        
        return res

